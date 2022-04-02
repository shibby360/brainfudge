class UnknownSymbolError(Exception):
  pass
class InvalidNumberError(Exception):
  pass
def bf(code):
  """

  Interpret some BrainFudge.

  """
  counters = None
  letts = None
  counters = {}
  for i in range(0, 21):
    counters[i] = 0
  counters['input'] = ''
  letts = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
  def lettify(item):
    toret = ''
    item = str(item)
    if item in letts:
      toret += letts[item]
    else:
      pass
    return toret
  def nummify(item):
    toret = ''
    if type(item) != int:
      if item.isnumeric():
        return int(item)
      else:
        for i in item:
          if i in item:
            toret += letts.index(i)
          else:
            toret += ''
      return int(toret)
    else:
      return item
  #Basic vars
  output = ''
  currCounter = 0
  currCounterVal = counters[currCounter]
  #Math var
  stg2opprtionnum = 1
  #Comment var
  commentmode = False
  #Mode vars
  lettmode = False
  nummode = True
  #Loop vars
  loopmode = False
  toloop = ''
  loopcount = ''
  loopnummode = False
  for i in code:
    if loopmode:
      if loopnummode:
        if i.isnumeric():
          loopcount += i
        elif i == ')':
          for i in range(int(loopcount)):
            for k in toloop:
              if k == 'a' or k == 'A':
                for j in counters:
                  def low(str):
                    return str.lower()
                  def up(str):
                    return str.upper()
                  if k == 'a':
                    func = low
                  elif k == 'A':
                    func = up
                  if j == 'input':
                    break
                  if type(counters[j]) == int:
                    if counters[j] > 26:
                      continue
                    counters[j] = func(letts[counters[j]])
                  else:
                    counters[j] = func(letts[letts.index(counters[j])])
              elif k == '0':
                for j in counters:
                  if j == 'input':
                    break
                  if type(counters[j]) == int:
                    counters[j] = counters[j]
                  else:
                    counters[j] = letts.index(counters[j])
              elif k == '>':
                if currCounter == 20:
                  currCounter = 'input'
                else:
                  currCounter += 1
              elif k == '<':
                if currCounter == 'input':
                  currCounter = 20
                else:
                  currCounter -= 1
              elif k == '/':
                currCounter = 20
              elif k == '\\':
                currCounter = 0
              elif k == '+':
                if currCounter != 'input':
                  counters[currCounter] += 1
              elif k == '-':
                if currCounter != 'input':
                  counters[currCounter] -= 1
              elif k == 'o':
                counters[currCounter] = 0
              elif k == '=':
                print(currCounterVal, end='')
                output += str(currCounterVal)
              elif k == '^':
                print(currCounter, end='')
                output += str(currCounter)
              elif k == '?':
                counters['input'] = input(str(currCounterVal) + '?: ')
              elif k == '&':
                stg2opprtionnum += 1
              elif k == '!':
                stg2opprtionnum -= 1
              elif k == '*':
                if counters[currCounter] != 'input':
                  counters[currCounter] *= stg2opprtionnum
              elif k == '`':
                if counters[currCounter] != 'input':
                  counters[currCounter] /= stg2opprtionnum
                  counters[currCounter] = round(counters[currCounter])
              elif k == '#':
                if currCounter != 'input':
                  if currCounter == 20:
                    counters[0] = currCounterVal
                  else:
                    counters[currCounter+1] = currCounterVal
              else:
                raise UnknownSymbolError('Symbol Unknown')
              currCounterVal = counters[currCounter]
          loopmode = False
          toloop = ''
          loopcount = ''
          loopnummode = False
        else:
          raise InvalidNumberError('Invalid Number')
      else:
        if i == '_':
          loopnummode = True
        else:
          toloop += i
    elif commentmode:
      if i == '}':
        commentmode = False
    else:
      if i == 'a' or i == 'A':
        def low(str):
          return str.lower()
        def up(str):
          return str.upper()
        if i == 'a':
          func = low
        elif i == 'A':
          func = up
        for j in counters:
          if j == 'input':
            break
          if type(counters[j]) == int:
            counters[j] = func(letts[counters[j]])
          else:
            counters[j] = func(letts[letts.index(counters[j])])
      elif i == '0':
        for j in counters:
          if j == 'input':
            break
          if type(counters[j]) == int:
            counters[j] = counters[j].lower()
          else:
            counters[j] = letts.index(counters[j].lower())
      elif i == '>':
        if currCounter == 20:
          currCounter = 'input'
        else:
          currCounter += 1
      elif i == '<':
        if currCounter == 'input':
          currCounter = 20
        else:
          currCounter -= 1
      elif i == '/':
        currCounter = 20
      elif i == '\\':
        currCounter = 0
      elif i == '+':
        if currCounter != 'input':
          counters[currCounter] += 1
      elif i == '-':
        if currCounter != 'input':
          counters[currCounter] -= 1
      elif i in ['o', 'O']:
        counters[currCounter] = 0
      elif i == '=':
        print(currCounterVal, end='')
        output += str(currCounterVal)
      elif i == '^':
        print(currCounter, end='')
        output += str(currCounter)
      elif i == '?':
        counters['input'] = input(str(currCounterVal) + '?: ')
      elif i == '&':
        stg2opprtionnum += 1
      elif i == '!':
        stg2opprtionnum -= 1
      elif i == '*':
        if counters[currCounter] != 'input':
          counters[currCounter] *= stg2opprtionnum
      elif i == '`':
        if counters[currCounter] != 'input':
          counters[currCounter] /= stg2opprtionnum
          counters[currCounter] = round(counters[currCounter])
      elif i == '#':
        if currCounter != 'input':
          if currCounter == 20:
            counters[0] = currCounterVal
          else:
            counters[currCounter+1] = currCounterVal
      elif i == '(':
        loopmode = True
      elif i == '{':
        commentmode = True
      else:
        raise UnknownSymbolError('Symbol Unknown')
      currCounterVal = counters[currCounter]
import sys
bf(sys.argv[1])
