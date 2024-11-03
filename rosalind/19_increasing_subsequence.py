import marimo

__generated_with = "0.9.8"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## [Longest Increasing Subsequence](https://rosalind.info/problems/lgis/)

        ### Background
        One very simple way of comparing genes from two chromosomes is to search for the largest collection of genes that are found in the same order in both chromosomes. To do so, we will need to apply our idea of permutations.

        Say that two chromosomes share `n` genes; if we label the genes of one chromosome by the numbers 1 through `n` in the order that they appear, then the second chromosome will be given by a permutation of these numbered genes.

        To find the largest number of genes appearing in the same order, we need only to find the largest collection of increasing elements in the permutation.

        ### Problem
        A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2). A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease.

        For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

        **Given:** A positive integer `n ≤ 10000` followed by a permutation π of length `n`.

        **Return:** A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

        ### Example
        Input:
        ```
        5
        5 1 4 2 3
        ```

        Output:
        ```
        1 2 3
        5 4 2
        ```
        """
    )
    return


@app.cell
def __():
    def longest_increasing_subsequence(pi: list, inc=True) -> list:
        """
        Finds the longest increasing or decreasing subsequence in pi.
        Video that helped: https://www.youtube.com/watch?v=aPQY__2H3tE

        For reference, with input [5, 3, 6, 8, 9, 2, 1, 10], we get:

        lis = [1, 1, 2, 3, 4, 1, 1, 5]
        prev = [-1, -1, 0, 2, 3, -1, -1, 4]

        Args:
            pi (list): Permutation of length n, where n <= 10,000
            inc (bool, default True): Whether to return the longest
            increasing or decreasing subsequence

        Returns:
            list: Longest increasing or decreasing subsequence in pi.
        """

        lis = [1] * len(pi)  # Track lengths of valid subsequences
        prev = [-1] * len(
            pi
        )  # Track indices of numbers that make a greater subsequence
        max_len = 1
        end = 0

        # Compare each integer pi[i] with all previous integers pi[j]
        for i in range(1, len(pi)):
            for j in range(i):
                # While the longest subsequence at index i has not been attained,
                if lis[i] < lis[j] + 1:
                    if (inc and pi[i] > pi[j]) or (not inc and pi[i] < pi[j]):
                        lis[i] = (
                            lis[j] + 1
                        )  # Update length of subsequence if pi[i] > pi[j]
                        prev[i] = (
                            j  # Track index of integer that contributes to subsequence
                        )

            # If a subsequence ending at index i > longest so far,
            if lis[i] > max_len:
                max_len = lis[i]  # Update longest subsequence so far
                end = i  # Update end index of subsequence

        result = []
        curr = end  # Start at the end index

        # Until we reach a -1 value in the prev array, we
        # reconstruct the subsequence from the end to the start.
        while curr >= 0:
            result.append(pi[curr])
            curr = prev[curr]  # Update end index pointer

        return result[::-1]

    def longest_decreasing_subsequence(pi: list):
        return longest_increasing_subsequence(pi, inc=False)
    return longest_decreasing_subsequence, longest_increasing_subsequence


@app.cell
def __(longest_decreasing_subsequence, longest_increasing_subsequence):
    nums = ""
    with open("./rosalind/sample_datasets/19_permutation.txt") as file:
        nums = file.readlines()[0]
    pi = nums.split(" ")
    pi = [int(x) for x in pi]
    inc = longest_increasing_subsequence(pi)
    dec = longest_decreasing_subsequence(pi)
    return dec, file, inc, nums, pi


@app.cell
def __(inc):
    _inc = " ".join([str(x) for x in inc])
    _inc
    return


@app.cell
def __(dec):
    _dec = " ".join([str(x) for x in dec])
    _dec
    return


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
