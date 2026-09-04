
class Solution:

    def encode(self, strs: List[str]) -> str:
        # naive
        encoded_string = ""

        # come up with delimiter
        for string in strs:
            encoded_string += self.get_ascii_for_word(string)
            encoded_string += "x"
        return encoded_string

    def get_ascii_for_word(self, string: str) -> str:
        combined_string = ""
        for char in string:
            combined_string += f"{ord(char):03d}"
        return combined_string

    def get_string_from_ascii(self, string: str) -> str:
        combined_string = ""
        for i in range(0, len(string), 3):
            combined_string += chr(int(string[i: i+3: 1]))
        return combined_string

    def decode(self, s: str) -> List[str]:
        # naive decoder
        decoded_list = []
        decoded_list = s.split("x")
        for i in range(0, len(decoded_list)):
            decoded_list[i] = self.get_string_from_ascii(decoded_list[i])

        decoded_list.pop()
        return decoded_list