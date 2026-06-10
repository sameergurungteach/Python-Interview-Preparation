def check_duplicates(str):
    result = " "
    for x in str:
          if x not in result:
            result += x
    return result

print(check_duplicates("programming"))



