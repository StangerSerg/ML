import numpy as np
from numpy.linalg import norm
from typing import Union, Optional

ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET_SIZE = len(ALPHABET)
ALPHABET_CACHE = {char: index for index, char in enumerate(ALPHABET)}


class CosineComparer:
    def __init__(self, ignore_non_alpha: bool = True, normalize_similarity: bool = True):
        """
        Args:
            ignore_non_alpha: Игнорировать символы не из алфавита
        """
        self.ignore_non_alpha = ignore_non_alpha

    def _vectorize(self, word: str) -> np.ndarray:
        """Преобразует слово в частотный вектор"""
        word_list = [0] * ALPHABET_SIZE

        for char in word.lower():
            idx = ALPHABET_CACHE.get(char)
            if idx is not None:
                word_list[idx] += 1
            elif not self.ignore_non_alpha:
                # Пока заглушка
                pass

        return np.array(word_list)

    def _calculate_similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
        """Вычисляет косинусное сходство между векторами"""
        norm1 = norm(vec1)
        norm2 = norm(vec2)

        if norm1 == 0 or norm2 == 0:
            return 0.0

        similarity = (vec1 @ vec2) / (norm1 * norm2)

        return float(similarity)

    def compare(self,
                first_word: str,
                second_word: str,
                mode: Union[int] = 0,
                sharpness: float = 0.9,
                return_float: bool = False) -> Union[str, bool, float]:
        """
        Сравнивает два слова

        Args:
            first_word: Первое слово
            second_word: Второе слово
            mode: 0 - вернуть строку с процентом,
                  1 - вернуть булево значение (>= sharpness)
                  2 - вернуть кортеж (булево, процент)
            sharpness: Порог для mode=1 (0.0 - 1.0)
            return_float: Вернуть float значение вместо форматированной строки для mode=0

         Returns:
            Зависит от параметров:
            - mode=0, return_float=False: str (например, "similarity 75.50%")
            - mode=0, return_float=True: float (например, 0.755)
            - mode=1: bool (True если similarity >= sharpness)
            - mode=2: Tuple[bool, float] (результат проверки и само значение)
        """

        # Валидация
        if not isinstance(first_word, str):
            raise ValueError(f"{first_word} is not string!")
        if not isinstance(second_word, str):
            raise ValueError(f"{second_word} is not string!")

        # Вычисляем similarity
        vec1 = self._vectorize(first_word)
        vec2 = self._vectorize(second_word)
        similarity = self._calculate_similarity(vec1, vec2)

        # Обработка разных режимов
        match mode:

            case 0:
                if return_float:
                    return similarity
                return f"similarity {similarity:.2%}"
                
            case 1:
                return similarity >= sharpness
                
            case 2:
                return similarity >= sharpness, similarity
                
            case _:
                raise ValueError(f"mode is {mode}, should be 0, 1, or 2")
