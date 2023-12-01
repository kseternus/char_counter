def chr_count(word):
    count = {}
    for i in word:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    return print(count)


chr_count('honorificabilitudinitatibus')
