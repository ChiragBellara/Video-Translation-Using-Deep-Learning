from flask import Flask, redirect, url_for, render_template, request, Response
app = Flask(__name__)

out1 = "Assembly. A low-level programming language designed to simplify the instructions fed into a computer's CPU. In other words, it's a human readable abstraction on top of machine code, so programmers don't have to manually count ones and zeros. The first assembly language was created by Kathleen Booth in 1947 for the all-purpose electronic computer. Over the next decade, it evolved into many different formats to power the supercomputers of the day, like the IBM 7090, which had a $20 million price tag in today's dollars. Writing code in assembly was standard until the emergence of high-level languages, like Fortran, a few years later. However..."
out2 = "काहू तो अच्छा, नाओ तो ज्यादा अच्छा। यदि चीजें आपकी इच्छानुसार होती हैं, तो यह अच्छा है। लेकिन अगर वे ऐसा नहीं करते, तो यह और भी अच्छा है। मैं हर समय अपने पिता को उद्धृत करता रहता हूं और मुझे यकीन है कि मैंने ऐसा लाखों बार किया है। पहली चीजों में से एक जो उन्होंने मुझे सिखाई वह थी, मन काहू तो अच्छा, नाव तो ज्यादा अच्छा। यदि चीजें आपकी इच्छानुसार होती हैं, तो यह अच्छा है। लेकिन अगर वे ऐसा नहीं करते, तो यह और भी अच्छा है। और मैं इसे कभी नहीं समझ सका. और जब मैंने उनसे पूछा, तो उन्होंने कहा, यदि वे आपकी इच्छा के अनुसार नहीं हो रहे हैं, तो वे किसी दैवीय शक्ति की इच्छा के अनुसार हो रहे हैं। और वह दैवीय शक्ति कभी भी आपके बारे में बुरा नहीं सोचेगी। इसलिए आपको इसे बेहतर मानकर इसका सम्मान करना होगा। तो अगर चीजें काम करतीं, तो मैंने कहा, ठीक है, अगर वे नहीं होतीं, तो मुझे लगता कि कोई दैवीय शक्ति या दिव्यता थी जो नहीं चाहती थी कि मैं ऐसा करूं। और शायद किसी अन्य अवसर की प्रतीक्षा करें. दूसरी बात जो उन्होंने मुझसे कही, वह यह थी कि जब मैं उस समय बहुत संघर्ष कर रहा था, तो मैंने कहा, आप जानते हैं, पला संघर्ष जीवन मैं। तो उन्होंने कहा, जीप्ता जीवन हीथप्तकसंगर्षा। मैं उससे कहता था, तुम्हें पता है, जीवन एक संघर्ष है। और वे कहते थे, जब तक जीवन है, संघर्ष रहेगा। मुझे लगता है कि अगर हम इस कारक को स्वीकार कर लें, तो आपका जीवन कभी आसान नहीं होगा। कुछ और होने वाला है. तो उस पर किसी प्रकार की निराशा में बैठने के बजाय, जागरूक रहें कि कल एक और चुनौती है, एक और दिन है, जो लाभदायक साबित हो सकता है, जो नहीं भी हो सकता है। लेकिन आख़िरकार एक और दिन आएगा जब आप फिर से प्रयास करना शुरू कर सकेंगे। मेरे दिमाग के पिछले हिस्से में वो बदसूरत पल होंगे जिन्होंने मुझे परेशान कर दिया था। और उनके दोबारा उभरने का डर ही शायद मुझे हर दिन प्रेरित करता है।"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/admin/")
def admin():
    return redirect(url_for("home"))


@app.route("/video/", methods=["GET", "POST"])
def getURL():
    videoURL = request.form.get("videoUrl")
    return render_template('index.html', WhisperOutcome=out1, TranslationOutcome=out2)


@app.route('/getAudioFile')
def getAudioFile():
    def generate():
        with open("static/StarWars60.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")


if __name__ == "__main__":
    app.run()
