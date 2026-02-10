class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        output = []
        output.append(celsius + 273.15)
        output.append(celsius * 1.80 + 32.00)
        return output