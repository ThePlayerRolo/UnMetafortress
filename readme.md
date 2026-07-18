# The Un-Metafortress Project

A project to replace of all the Metafortress affected code in Kirby's Return To Dreamland with non Metafortress variants.

> [!Warning]
> This project is NOT meant to aid with piracy. An existing copy of the game is required to use the resources present here. (Even for the MAP file!)

## The project contains the following:
- A code patch to use with things such as dolphin
- Info on each of the currently attempted/un-MetaFortressed functions
- A "patch" file to apply to the MAP (for analysis in the future)
- A configure.py system akin to dtk-template for progress and code patch generation

TODO:
Add a program/file to patch the dol file with the Un-MetaFortressed functions.
Use MappingStuffOut.txt to map out the rest of the metafortressed functions

Build and Install Dolphin Patch:
    1. git clone the Repo
    2. Run configure.py generate
    3. In out/PatchCode are your patches.
    4. Install in dolphin and enable them. BE SURE TO DISABLE THE OG "BYPASS METAFORTRESS" PATCH! There can be conflicts
    5. Enjoy!

Credits:
crediar for the og Bypass Metafortress, which is used for unfinished functions