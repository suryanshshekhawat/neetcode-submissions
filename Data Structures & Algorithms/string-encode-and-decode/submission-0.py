class Solution:

    def encode(self, strs: List[str]) -> str:
        # naive
        encoded_string = ""
        for string in strs:
            encoded_string += string
            encoded_string += " "
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # naive decoder
        decoded_list = s.split(" ")
        decoded_list.pop()
        return decoded_list