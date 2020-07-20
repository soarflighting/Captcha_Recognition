import numpy as np

def text2vec(text):
    """
    文本转向量
    Parameters:
        text:文本
    Returns:
        vector:向量
    """
    if len(text) > 4:
        raise ValueError('验证码最长4个字符')

    vector = np.zeros(4 * 63)
    def char2pos(c):
        if c =='_':
            k = 62
            return k
        k = ord(c) - 48
        if k > 9:
            k = ord(c) - 55
            if k > 35:
                k = ord(c) - 61
                if k > 61:
                    raise ValueError('No Map')
        return k
    for i, c in enumerate(text):
        idx = i * 63 + char2pos(c)
        vector[idx] = 1
    return vector

def vec2text(vec):
    """
    向量转文本
    Parameters:
        vec:向量
    Returns:
        文本
    """
    #找到vec中非零的位置
    char_pos = vec.nonzero()[0]
    text = []
    for i, c in enumerate(char_pos):
        char_at_pos = i #c/63
        char_idx = c % 63
        if char_idx < 10:
            char_code = char_idx + ord('0')
        elif char_idx < 36:
            char_code = char_idx - 10 + ord('A')
        elif char_idx < 62:
            char_code = char_idx - 36 + ord('a')
        elif char_idx == 62:
            char_code = ord('_')
        else:
            raise ValueError('error')
        text.append(chr(char_code))
    return "".join(text)

if __name__ == '__main__':
    vec = text2vec("bsvs")
    print(vec.nonzero()[0])
