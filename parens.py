def parse(tokens, *pairs):
    i = [0] # ugly hack due to no nonlocal

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
        if i[0] >= len(tokens):
            return True
        for o, c in pairs:
            if not accept(o):
                continue
            expression()
            expect(c)
            expression()
            return True
        return True

    expression()
    assert i[0] >= len(tokens)

if __name__ == '__main__':
    def shouldfail(*args):
        try:
            parse(*args)
        except:
            return
        raise Exception('Should have failed! [{!r}]'.format(arg))

    parse('', '()')
    parse('()', '()')
    parse('()()', '()')
    parse('()()()', '()')
    parse('(())', '()')
    parse('(())(()())', '()')
    shouldfail(')', '()')
    shouldfail(')(', '()')
    shouldfail('(()', '()')
    shouldfail('())(()', '()')
    shouldfail('())(()', '()')
    parse('()', '()', '{}')
    parse('({})', '()', '{}')
    shouldfail('{(})', '()', '{}')
    parse('({}ab)', '()', '{}', 'ab')
    shouldfail('({a}b)', '()', '{}', 'ab')
