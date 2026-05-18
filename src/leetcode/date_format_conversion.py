from datetime import datetime

class Solution:
    def convert_from_input(self, in_format: str) -> str:
        date = datetime.strptime(in_format, "%m/%d/%Y")
        return date.strftime("%Y%m%d")

def main():
    solution = Solution()
    input = "05/26/1986"
    output = solution.convert_from_input(input)
    print(f'Input= {input}, Output= {output}')

if __name__ == "__main__":
    main()



