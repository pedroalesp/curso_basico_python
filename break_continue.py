def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue 
    #     print(contador)

    # for i in range(5000):
    #     print(i)
    #     if i == 3456:
    #         break

    frase = input("Escribe una frase: ")
    for caracter in frase:
        if caracter == "r":
            break
        else:
            print(caracter)


if __name__ == "__main__":
    run()