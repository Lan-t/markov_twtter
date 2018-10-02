
import text
import generate
import twitter
import time
import keys

t = []
for key in keys.keys:

    t.append(twitter.Api(key[0],key[1],key[2],key[3]))



data = text.make_data()


while True:

    for i in t:

        result = generate.generate(data)
        result = 'bot:' + result

        i.PostUpdate(result)

    time.sleep(60 * 10)