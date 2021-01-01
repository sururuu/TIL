def solution(phone_book):

    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            left, right = phone_book[i], phone_book[j]
            left = list(map(str, str(left)))
            right = list(map(str, str(right)))
            if len(left) < len(right):
                right = right[:len(left)]
                if left == right:
                    return False
            else:
                left = left[:len(right)]
                if left == right:
                    return False
    return True