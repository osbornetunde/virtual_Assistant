import wolframalpha

input = raw_input("Question: ")
app_id = "JYWTEJ-JLKTAVAER6"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print answer