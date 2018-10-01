
import text
import generate
import twitter
import time
import keys

twitter = []
for key in keys.keys:

    twitter.append(twitter.Api(key[0],key[1],key[2],key[3]))



data = text.make_data()


while True:

    for i in twitter:

        result = generate.generate(data)
        result = 'bot:' + result

        i.PostUpdate(result)

    time.sleep(60 * 10)