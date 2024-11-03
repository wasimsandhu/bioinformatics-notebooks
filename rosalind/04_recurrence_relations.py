import marimo

__generated_with = "0.9.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        ## [Rabbits and Recurrence Relations](https://rosalind.info/problems/fib/)

        ### Background
        A **sequence** is an ordered collection of objects (usually numbers), which are allowed to repeat. Sequences can be finite or infinite. Two examples are the finite sequence (π,−2‾√,0,π) and the infinite sequence of odd numbers (1,3,5,7,9,…).

        A **recurrence relation** is a way of defining the terms of a sequence with respect to the values of previous terms. In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, plus any new offspring.

        A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior.

        As a result, if F<sub>n</sub> represents the number of rabbit pairs alive after the nth month, then we obtain the Fibonacci sequence having terms F<sub>n</sub> that are defined by the recurrence relation F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub> (with F<sub>1</sub> = F<sub>2</sub> = 1 to initiate the sequence).

        When finding the nth term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n. This problem introduces us to the computational technique of **dynamic programming**, which successively builds up solutions by using the answers to smaller cases.

        ### Problem
        **Given:** Positive integers n ≤ 40 and k ≤ 5.

        **Return:** The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
        """
    )
    return


@app.cell
def __():
    def count_rabbit_pairs(months, pairs_per_litter=3, return_counts=False) -> int:
        """Returns number of rabbits present after n months and k pairs per litter."""

        # Keep running total of all rabbits
        total_pairs = 1
        adult_pairs = 0
        child_pairs = 1

        # Edge cases
        if months == 1:
            return 1

        if months == 2:
            return 4

        # For every month,
        for month in range(months - 1):
            # Existing adult pairs give birth to a litter of size k
            new_babies = adult_pairs * pairs_per_litter

            # All of the previous child rabbit pairs reach adulthood
            adult_pairs += child_pairs
            child_pairs = new_babies

            # Total = adults + children
            total_pairs += child_pairs

            if return_counts:
                print(
                    "Total",
                    total_pairs,
                    "\nAdults",
                    adult_pairs,
                    "\nChildren",
                    child_pairs,
                    "\n",
                )

        return total_pairs

    return (count_rabbit_pairs,)


@app.cell
def __(count_rabbit_pairs):
    rabbits = count_rabbit_pairs(5, 3, return_counts=True)
    print("Total rabbit pairs after 5 months:", rabbits)
    return (rabbits,)


@app.cell
def __():
    import ipytest

    ipytest.autoconfig()
    return (ipytest,)


@app.cell
def __():
    # magic command not supported in marimo; please file an issue to add support
    # %%ipytest
    #
    # def test_case_1():
    #     expected = 1
    #     actual = count_rabbit_pairs(1, 3)
    #     assert actual == expected
    #
    # def test_case_2():
    #     expected = 4
    #     actual = count_rabbit_pairs(2, 3)
    #     assert actual == expected
    #
    # def test_case_3():
    #     expected = 19
    #     actual = count_rabbit_pairs(5, 3)
    #     assert actual == expected
    return


@app.cell
def __(count_rabbit_pairs):
    print(count_rabbit_pairs(35, 3))
    return


@app.cell
def __():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
