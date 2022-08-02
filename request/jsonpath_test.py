from jsonpath import jsonpath
res={
    "name":"cjh"
}

test_name = jsonpath(res,'$..name')[0]
print(test_name)