FROM python:3.9

ADD . .

RUN pip install pyTelegramBotAPI python-dotenv pytest-playwright loguru
RUN python -m playwright install
RUN python -m playwright install-deps
RUN pip install TikTokApi-5.2.2.tar.gz

CMD [ "python", "./tiktok.py" ]