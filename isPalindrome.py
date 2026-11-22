class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Saltamos caracteres no alfanuméricos por la izquierda
            while left < right and not s[left].isalnum():
                left += 1
            # Saltamos caracteres no alfanuméricos por la derecha
            while left < right and not s[right].isalnum():
                right -= 1

            # Comparamos ignorando mayúsculas/minúsculas
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
