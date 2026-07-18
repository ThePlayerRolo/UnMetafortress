from pathlib import Path
import os

# fake enum lol
NoProgress = 0
WorkInProgress = 1
Done = 2


class Function:
    def __init__(self, progress: int, funcSignature: str, folderName: str) -> None:
        self.progress = progress
        self.funcSignature = funcSignature
        self.folderName = folderName


class Config:
    def __init__(self) -> None:
        self.functions = []
        self.unNotedFunctions = 0
        self.funcAmount = 0

    def setFunctions(self, funcAmount: int, functionList: list[Function]) -> None:
        self.functions = functionList
        self.funcAmount = funcAmount
        self.unNotedFunctions = self.funcAmount - len(self.functions)

    def getDoneFunctions(self) -> int:
        doneFunctions = 0
        for i in self.functions:
            if i.progress == Done:
                doneFunctions += 1
        return doneFunctions

    def getProgressPercent(self) -> float:
        return round((self.getDoneFunctions() / self.funcAmount) * 100.0, 2)

    def progressReport(self) -> None:
        print("The Un-Metafortress Project Report\n")
        print("Current progress: {}% ({} out of {} functions).".format(
            self.getProgressPercent(), self.getDoneFunctions(),
            self.funcAmount))

    def generate_doneFuncs(self) -> str:
        finalStr = ""
        for i in self.functions:
            if i.progress != Done:
                continue
            filePath = Path("Functions/{}".format(i.folderName))
            f = open(filePath / "DolphinPatch.txt")
            finalStr += f.read() + "\n"
            f.close()
        return finalStr

    def generate(self) -> None:
        outDir = Path("out")
        if not os.path.exists(outDir):
            os.makedirs(outDir)

        f = open(outDir / "PatchCode.txt", 'w')
        f.write("[OnFrame]\n$Replace Metafortress [The Un-Metafortress Project]\n")
        f.write(self.generate_doneFuncs())
        f.write("\n")
        unmappedFunctionsFile = open(Path("Functions/") /  "CrediarPatch.txt")
        f.write(unmappedFunctionsFile.read() + "\n")
        f.close()
