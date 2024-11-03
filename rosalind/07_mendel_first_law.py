import marimo

__generated_with = "0.9.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        ## [Mendel's First Law](https://rosalind.info/problems/iprb/)

        ### Background
        **Probability** is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a random variable, which is simply a variable that can take a number of different distinct outcomes depending on the result of an underlying random process.

        For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X represent the random variable corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by Pr(X=red) = 3 / 5 and Pr(X=blue) = 2 / 5.

        An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes.

        ### Problem
        **Given:** Three positive integers `k`, `m`, and `n`, representing a population containing k+m+n organisms: `k` individuals are homozygous dominant for a factor, `m` are heterozygous, and `n` are homozygous recessive.

        **Return:** The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

        ### Example
        Input:
        ```
        k = 2, m = 2, n = 2
        ```

        Output:
        ```
        0.78333
        ```
        """
    )
    return


@app.cell
def __():
    from itertools import combinations

    def dominant_allele_probability(k: int, m: int, n: int):
        """
        Returns the probability that two randomly selected mating organisms will
        produce offspring possessing a dominant allele in a population of k homozygous
        dominant, m heterozygous, and n homozygous recessive individuals.

        Args:
            k (int): Homozygous dominant individuals
            m (int): Heterozygous individuals
            n (int): Homozygous recessive individuals
        """

        dominant = ["GG" for x in range(k)]
        heterozygous = ["Gg" for x in range(m)]
        recessive = ["gg" for x in range(n)]
        population = dominant + heterozygous + recessive

        comb_recessive_2 = combinations(heterozygous + recessive, 2)
        comb_recessive_2 = [
            x for x in comb_recessive_2 if x != ("Gg", "Gg") and x != ("gg", "gg")
        ]

        recessive_1 = len(list(combinations(heterozygous, 2)))
        recessive_2 = len(comb_recessive_2)
        recessive_3 = len(list(combinations(recessive, 2)))

        comb_recessive = 0.25 * recessive_1 + 0.5 * recessive_2 + recessive_3
        comb_total = len(list(combinations(population, 2)))

        prob_recessive = comb_recessive / comb_total
        return 1 - prob_recessive

    return combinations, dominant_allele_probability


@app.cell
def __(dominant_allele_probability):
    import ipytest

    ipytest.autoconfig()

    def test_case_1():
        prob_dominant = dominant_allele_probability(2, 2, 2)
        assert prob_dominant == 0.7833333333333333

    ipytest.run()
    return ipytest, test_case_1


@app.cell
def __(mo):
    mo.md(
        r"""
        ### Explanation
        Population for above values: `[GG, GG, Gg, Gg, gg, gg]`

        Total combinations of parents:
        - `GG x GG` (1)
        - `GG x Gg` (4)
        - `GG x gg` (4)
        - `Gg x Gg` (1)
        - `Gg x gg` (4)
        - `gg x gg` (1)

        Combinations of parents that will lead to a recessive offspring:
        - `Gg x gg`, of which there are 1, or `combinations([Gg, Gg], 2)` or `recessive_1`
            - From this, there is a 25% probability of a recessive offspring
        - `Gg x gg`, of which there are 4, or `combinations([Gg, Gg, gg, gg], 2)` or `recessive_2`
            - From this, there is a 50% probability of a recessive offspring
        - `gg x gg`, of which there are 1, or `combinations([gg, gg], 2)`
            - From this, there is a 100% probability of a recessive offspring or `recessive_3`

        The probability of a recessive offspring, in terms:

        `prob_recessive = comb_recessive / comb_total`, where

        `comb_recessive = recessive_1 + recessive_2 + recessive_3`, and

        `comb_total = combinations([GG, GG, Gg, Gg, gg, gg], 2)`

        Then, the probability of a dominant offspring is simply:

        `prob_dominant = 1 - prob_recessive`
        """
    )
    return


@app.cell
def __(dominant_allele_probability):
    dominant_allele_probability(21, 17, 19)
    return


@app.cell
def __():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
