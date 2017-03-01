
def parse(tokens):
    i = [0] # ugly hack due to no nonlocal

    def end():
        return i[0] >= len(tokens)

    def sym():
        return tokens[i[0]]

    def accept(s):
        if sym() == s:
            i[0] += 1
            return True
        return False

    def expect(s):
        if not accept(s):
            raise Exception('Unexpected symbol [{!r}], expected [{!r}] at position [{}]'.format(sym(), s, i[0]))

    def expression():
        if end() or not accept('('):
            return True
        expression()
        expect(')')
        expression()
        return True

    expression()
    assert end()

if __name__ == '__main__':

    def shouldfail(arg):
        try:
            parse(arg)
        except:
            return
        raise Exception('Should have failed! [{!r}]'.format(arg))

    parse('')
    parse('()')
    parse('()()')
    parse('()()()')
    parse('(())')
    parse('(())(()())')
    shouldfail(')')
    shouldfail(')(')
    shouldfail('(()')
    shouldfail('())(()')
    shouldfail('())(()')
    
