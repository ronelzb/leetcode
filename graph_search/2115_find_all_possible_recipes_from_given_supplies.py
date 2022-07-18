# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
# tags: #google, #graph, #hash_table, #topological_sort
#
# Solution: Topological sort
# For each recipe, count its dependent ingredients as in degree,
# store each ingredient dependent to a recipe in a dictionary.
# Use the supplies as the starting points of topological sort, one option is to convert supplies list to a queue
# The topological sort will be based on the supplies first given, we will decrease the in degree of recipes
# and whenever in-degree reaches zero it means we can create the recipe, so we add that recipe to the supplies_left.
# Time complexity : O(m*n) m=recipes n=ingredients, Space complexity: O(n)
from collections import defaultdict, deque

from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredients_to_recipe = defaultdict(list)  # graph
        in_degree = dict()

        for i, recipe in enumerate(recipes):
            n = len(ingredients[i])
            in_degree[recipe] = n
            for j in range(n):
                ingredients_to_recipe[ingredients[i][j]].append(recipe)

        # Topological sort
        allowed_recipes = []
        supplies_left = deque(supplies)
        while supplies_left:
            ing_supplied = supplies_left.popleft()

            for recipe in ingredients_to_recipe.pop(ing_supplied, []):
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    supplies_left.append(recipe)
                    allowed_recipes.append(recipe)

        return allowed_recipes


if __name__ == '__main__':
    sol = Solution()
    print(sol.findAllRecipes(
        recipes=["bread", "sandwich", "burger"],
        ingredients=[["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
        supplies=["yeast", "flour", "meat"]
    ))  # ["bread","sandwich","burger"]

    print(sol.findAllRecipes(
        recipes=["ju", "fzjnm", "x", "e", "zpmcz", "h", "q"],
        ingredients=[
            ["d"], ["hveml", "f", "cpivl"], ["cpivl", "zpmcz", "h", "e", "fzjnm", "ju"],
            ["cpivl", "hveml", "zpmcz", "ju", "h"],
            ["h", "fzjnm", "e", "q", "x"],
            ["d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"],
            ["f", "hveml", "cpivl"]],
        supplies=["f", "hveml", "cpivl", "d"],
    ))  # ['fzjnm', 'q', 'ju']
