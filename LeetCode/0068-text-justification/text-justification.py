from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # char_count == number of chars in temp_list - spaces
        temp_list, final_list, char_count = [], [], 0
        # print(temp_list, final_list, char_count)
        for current_word in words:
            if len(current_word) + len(temp_list) + char_count > maxWidth:
                # NOTE: need to append here not += since temp_list is string
                # handling spaces between words
                for i in range(maxWidth - char_count):
                    temp_list[i % (len(temp_list) - 1 or 1)] += " "
                final_list.append("".join(temp_list))
                temp_list, char_count = [], 0
            # print(f"Current final list is {final_list}")
            temp_list += [current_word]
            char_count += len(current_word)
            # handling last line to be left-justified
        return final_list + [" ".join(temp_list).ljust(maxWidth)]
        # final_list.append("".join(temp_list) + "\n")
        # print(f"Current final list is {final_list}")


sol = Solution()
words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16
result = sol.fullJustify(words, maxWidth)
print(result)
