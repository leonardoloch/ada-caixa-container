def test():
    assert False


if __name__ == "__main__":
    try:
        test()
        print("Test foi um sucesso")
    except AssertionError:
        print("Teste falhou")
        exit(1)