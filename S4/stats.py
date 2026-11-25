def moyenne(nombres):
    return sum(nombres) / len(nombres)


def minimum(nombres):
    return min(nombres)


def maximum(nombres):
    return max(nombres)

if __name__ == "__main__":
    valeur_test = [10, 12, 14]
    print("Test du module")
    print(moyenne(valeur_test))