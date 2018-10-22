FROM python:3.6

RUN useradd -ms /bin/bash bot
ADD . /home/bot/pbstaxbot
RUN pip --no-cache-dir --quiet install -r /home/bot/pbstaxbot/requirements.txt
USER bot

CMD python /home/bot/pbstaxbot/bot.py
