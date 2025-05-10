import marimo

__generated_with = "0.9.32"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def __(experimental_spectrum, pl, render_mass_spectrum):
    df_experimental = pl.DataFrame(
        {
            "m/z": experimental_spectrum.peaks.mz,
            "Intensity": experimental_spectrum.peaks.intensities,
        },
    )
    render_mass_spectrum(
        df_experimental,
        title="Query Mass Spectrum",
    )
    return (df_experimental,)


@app.cell(hide_code=True)
def __(library_dropdown, mo):
    search_button = mo.ui.run_button(
        label="Search spectrum against library", full_width=True
    )
    mo.vstack([library_dropdown, search_button], gap=1)
    return (search_button,)


@app.cell
def __(experimental_spectrum, library_dropdown, mo, search, search_button):
    mo.stop(not search_button.value)
    spectral_matches = search(experimental_spectrum, library_dropdown.value)
    return (spectral_matches,)


@app.cell
def __(mo):
    GNPS_BASE_URL = "https://gnps-external.ucsd.edu/gnpslibrary/"
    spectral_libraries = {
        "GNPS (Full Library)": f"{GNPS_BASE_URL}/GNPS-LIBRARY.json",
        "GNPS NIH Clinical Collection 1": f"{GNPS_BASE_URL}/GNPS-NIH-CLINICALCOLLECTION1.json",
        "GNPS NIH Clinical Collection 2": f"{GNPS_BASE_URL}/GNPS-NIH-CLINICALCOLLECTION2.json",
        "GNPS Natural Products Library": f"{GNPS_BASE_URL}/GNPS-NIH-NATURALPRODUCTSLIBRARY.json",
    }
    library_dropdown = mo.ui.dropdown(
        spectral_libraries.keys(),
        value="GNPS NIH Clinical Collection 1",
        label="Choose spectral library to search against",
        full_width=True,
    )
    return GNPS_BASE_URL, library_dropdown, spectral_libraries


@app.cell(hide_code=True)
def __():
    sample_spectrum = [[58.520630,152.000000],[117.075005,172.000000],[132.985809,140.000000],[154.056915,144.000000],[164.765015,176.000000],[166.052567,172.000000],[184.071991,180.000000],[187.036133,120.000000],[200.869888,160.000000],[202.053543,144.000000],[203.592667,144.000000],[206.940308,208.000000],[207.040527,144.000000],[213.455688,148.000000],[215.024490,184.000000],[216.035507,104.000000],[217.695801,160.000000],[226.705490,176.000000],[234.027725,292.000000],[235.032639,212.000000],[236.029327,148.000000],[249.051895,120.000000],[256.052155,184.000000],[262.068085,168.000000],[263.063263,1272.000000],[264.067902,104.000000],[265.060120,284.000000],[265.082581,164.000000],[266.059082,180.000000],[266.156464,156.000000],[272.093323,148.000000],[275.057495,116.000000],[285.036560,216.000000],[289.045837,172.000000],[291.915588,180.000000],[300.917053,144.000000],[303.087402,168.000000],[316.554840,180.000000],[318.107635,144.000000],[320.120941,1372.000000],[320.911133,192.000000],[321.122620,320.000000],[322.117218,320.000000],[338.934357,160.000000],[339.095581,224.000000],[341.220947,176.000000],[362.153900,196.000000],[363.253113,176.000000],[364.111267,2448.000000],[365.115845,800.000000],[365.175079,156.000000],[366.111359,128.000000],[367.121185,192.000000],[401.043854,172.000000],[443.809967,164.000000]]
    return (sample_spectrum,)


@app.cell
def __(ms, np, sample_spectrum):
    experimental_spectrum = ms.Spectrum(
        mz=np.array(sample_spectrum)[:, 0],
        intensities=np.array(sample_spectrum)[:, 1],
    )
    experimental_spectrum = ms.filtering.normalize_intensities(
        experimental_spectrum
    )
    return (experimental_spectrum,)


@app.cell
def __(DATA_DIR_PATH, ms, requests, spectral_libraries):
    def search(
        query_spectrum: ms.Spectrum, spectral_library: str, top_n_matches: int = 5
    ):
        # Download and import spectral library
        library_path = DATA_DIR_PATH / f"{spectral_library}.json"

        if not library_path.exists():
            print(f"Downloading {spectral_library}...")
            response = requests.get(spectral_libraries[spectral_library])
            response.raise_for_status()
            with open(library_path, "wb") as f:
                f.write(response.content)

        print("Loading library...")
        library = ms.importing.load_from_json(library_path)

        # Apply filters to clean and enhance each spectrum
        print("Applying filters to library...")
        reference_spectra = []
        for spectrum in library:
            spectrum = ms.filtering.default_filters(spectrum)
            spectrum = ms.filtering.normalize_intensities(spectrum)
            reference_spectra.append(spectrum)

        # Calculate similarity scores against library
        print("Calculating similarity scores...")
        scores = ms.calculate_scores(
            references=reference_spectra,
            queries=[query_spectrum],
            similarity_function=ms.similarity.CosineGreedy(),
        )

        # Query library for user-inputted spectrum
        print("Searching for matches...")
        best_matches = scores.scores_by_query(
            query_spectrum, "CosineGreedy_score", sort=True
        )[:top_n_matches]
        print("Complete!")
        return best_matches
    return (search,)


@app.cell
def __(__file__):
    import pathlib
    import altair as alt
    import marimo as mo
    import matchms as ms
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    import polars as pl
    import requests
    from rdkit import Chem
    from rdkit.Chem import Draw
    from plotly.subplots import make_subplots

    DATA_DIR_PATH = pathlib.Path(__file__).parent / "data"
    DATA_DIR_PATH.mkdir(parents=True, exist_ok=True)

    PUBCHEM_API_BASE_URL = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
    return (
        Chem,
        DATA_DIR_PATH,
        Draw,
        PUBCHEM_API_BASE_URL,
        alt,
        go,
        make_subplots,
        mo,
        ms,
        np,
        pathlib,
        pl,
        px,
        requests,
    )


@app.cell(column=1, hide_code=True)
def __(mo, spectral_matches):
    match_names = [
        match.metadata["compound_name"] for match, _ in spectral_matches
    ]
    match_dropdown = mo.ui.dropdown(
        options=match_names,
        value=match_names[0],
        label="Select a match to view",
        full_width=True,
    )
    match_dropdown
    return match_dropdown, match_names


@app.cell
def __(
    df_experimental,
    match_dropdown,
    pl,
    render_head_to_tail,
    spectral_matches,
):
    selected_match = [
        (match, score)
        for match, score in spectral_matches
        if match.metadata["compound_name"] == match_dropdown.value
    ][0]
    df_reference = pl.DataFrame(
        {
            "m/z": selected_match[0].peaks.mz,
            "Intensity": selected_match[0].peaks.intensities,
        },
    )
    render_head_to_tail(df_experimental, df_reference)
    return df_reference, selected_match


@app.cell
def __(px):
    def render_mass_spectrum(df_peaks, title="Experimental Spectrum", range=None):
        """Render mass spectrum m/z vs. intensity plot."""
        if range is None:
            min_mz = df_peaks["m/z"].min() - 10
            max_mz = df_peaks["m/z"].max() + 10
            range = [min_mz, max_mz]

        plot = px.bar(df_peaks, title=title, x="m/z", y="Intensity", height=400)
        plot.update_layout(
            showlegend=False,
            transition_duration=500,
            clickmode="event",
            margin=dict(t=75, b=75, l=0, r=0),
        )
        plot.update_xaxes(title="", range=range, side="bottom")
        plot.update_yaxes(title="")
        plot.update_traces(
            width=1,
            textposition="outside",
            hovertemplate="m/z: %{x}<br>Intensity: %{y}<br>",
        )

        return plot
    return (render_mass_spectrum,)


@app.cell
def __(go, make_subplots):
    def render_head_to_tail(df_head, df_tail):
        """Render head-to-tail plot for spectral comparison."""

        min_mz = min(df_head["m/z"].min(), df_tail["m/z"].min()) - 10
        max_mz = max(df_head["m/z"].max(), df_tail["m/z"].max()) + 10

        plot = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0)

        plot.append_trace(
            go.Bar(
                x=df_head["m/z"],
                y=df_head["Intensity"],
                marker=dict(color="rgb(0, 123, 255)"),
            ),
            row=1,
            col=1,
        )
        plot.append_trace(
            go.Bar(
                x=df_tail["m/z"],
                y=df_tail["Intensity"],
                marker=dict(color="rgb(220, 53, 69)"),
            ),
            row=2,
            col=1,
        )

        plot.update_xaxes(range=[min_mz, max_mz])
        plot.update_xaxes(showticklabels=True, row=1, col=1)

        plot.update_xaxes(title="Experimental", row=1, col=1)
        plot.update_xaxes(title="Reference", row=2, col=1)
        plot.update_yaxes(autorange="reversed", row=2, col=1)

        plot.update_traces(
            width=1, hovertemplate="m/z: %{x}<br>Intensity: %{y}<br>"
        )
        plot.update_layout(
            height=400,
            showlegend=False,
            margin=dict(t=0, b=0, l=0, r=0),
            xaxis={"side": "top"},
        )

        return plot
    return (render_head_to_tail,)


@app.cell(column=2, hide_code=True)
def __(Chem, Draw, PUBCHEM_API_BASE_URL, match_dropdown, requests):
    compound_name = match_dropdown.value.lower()
    endpoint = f"{PUBCHEM_API_BASE_URL}/compound/name/{compound_name}/property/CanonicalSMILES/JSON"

    smiles = ""
    if compound_name:
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            smiles = response.json()["PropertyTable"]["Properties"][0][
                "CanonicalSMILES"
            ]
        except Exception as e:
            print(f"Error fetching SMILES for '{compound_name}': {e}")

    molecule = Chem.MolFromSmiles(smiles)
    Draw.MolsToImage(
        mols=[molecule], subImgSize=(400, 400), legends=[compound_name]
    )
    return compound_name, endpoint, molecule, response, smiles


@app.cell
def __(fetch_pubchem_properties, match_dropdown, mo):
    mo.ui.table(
        fetch_pubchem_properties(match_dropdown.value), label="PubChem properties"
    )
    return


@app.cell
def __(pl, requests):
    def fetch_pubchem_properties(compound_name):
        """Fetches properties of a compound from PubChem using its name."""
        base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
        endpoint = f"{base_url}/compound/name/{compound_name}/property/MolecularFormula,MolecularWeight,ExactMass,InChIKey/JSON"

        try:
            # Fetch molecular formula, weight, and exact mass
            response = requests.get(endpoint)
            response.raise_for_status()
            data = response.json()

            properties = data["PropertyTable"]["Properties"][0]
            molecular_formula = properties.get("MolecularFormula")
            molecular_weight = properties.get("MolecularWeight")
            exact_mass = properties.get("ExactMass")
            inchikey = properties.get("InChIKey")

            # Fetch computed properties (section 3.1)
            computed_props_endpoint = (
                f"{base_url}/compound/name/{compound_name}/JSON"
            )
            computed_response = requests.get(computed_props_endpoint)
            computed_response.raise_for_status()
            computed_data = computed_response.json()

            computed_properties = computed_data.get("PC_Compounds", [{}])[0].get(
                "props", []
            )
            properties = {
                "molecular_formula": molecular_formula,
                "molecular_weight": molecular_weight,
                "exact_mass": exact_mass,
                "inchikey": inchikey,
                "computed_properties": [computed_properties],
            }
        except Exception as e:
            print(f"Error fetching properties for {compound_name}: {e}")
            return None

        return pl.DataFrame(properties, strict=False)
    return (fetch_pubchem_properties,)


if __name__ == "__main__":
    app.run()
