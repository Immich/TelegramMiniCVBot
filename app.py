import logging
import os

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from telebot.credentials import bot_token, URL

global bot
global TOKEN
global URL

PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
URL = URL
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

# Stages
#FIRST, SECOND, THIRD, FOURTH, FIFTH, SIXTH, SEVENTH = range(7)


# Callback data
# ONE, TWO, THREE, FOUR = range(4)


#### Command Handlers ####

# def start(update, context):
#    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm Michelle's bot, please talk to me!")
def start(update: Update, context: CallbackContext) -> None:
    """Send Message on '/start'."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User {} started the conversation.".format(user.first_name))
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).

    keyboard = [
        [
            InlineKeyboardButton("Short bio ⚡‍", callback_data="/bio"),
            InlineKeyboardButton("Work Experience 👩‍💻", callback_data="/work_exp")

        ],
        [
            InlineKeyboardButton("Personal Projects 💙", callback_data="/per_project"),
            InlineKeyboardButton("Awards/Honors 🏆", callback_data="/awards"),
        ],
        [
            InlineKeyboardButton("Skills 💻", callback_data="/skills"),
            InlineKeyboardButton("Languages 🌎", callback_data="/lan"),
        ],
        [
            InlineKeyboardButton("Blog 📄", callback_data="/blog"),
            InlineKeyboardButton("Contact 📧", callback_data="/contact"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text(
        "Hi, I am Michelle and this chat is for you to get to know more about me and my professional achievements and interests.\n"
        "Please select the option that you would like to know further:", reply_markup=reply_markup)


def menu(update: Update, context: CallbackContext) -> None:
    """Send Message on '/start'."""
    keyboard = [
        [
            InlineKeyboardButton("Short bio ⚡‍", callback_data="/bio"),
            InlineKeyboardButton("Work Experience 👩‍💻", callback_data="/work_exp")

        ],
        [
            InlineKeyboardButton("Personal Projects 💙", callback_data="/per_project"),
            InlineKeyboardButton("Awards/Honors 🏆", callback_data="/awards"),
        ],
        [
            InlineKeyboardButton("Skills 💻", callback_data="/skills"),
            InlineKeyboardButton("Languages 🌎", callback_data="/lan"),
        ],
        [
            InlineKeyboardButton("Blog 📄", callback_data="/blog"),
            InlineKeyboardButton("Contact 📧", callback_data="/contact"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("Choose:", reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == "/bio":
        bio(update, context)
        query.edit_message_text(text=f"You selected: {query.data}, if you want to see the menu again please type '/menu'")
    elif query.data == "/work_exp":
        work_exp(update, context)
        #query.edit_message_text(text=f"You selected: {query.data}, if you want to see the menu again please type '/menu'")
    elif query.data == "/per_project":
        per_project(update, context)
        query.edit_message_text(text=f"You selected: {query.data}, if you want to see the menu again please type '/menu'")
    elif query.data == "/awards":
        awards(update, context)
        query.edit_message_text(text=f"You selected: {query.data}, if you want to see the menu again please type '/menu'")
    elif query.data == "/skills":
        skills(update, context)
        query.edit_message_text(text=f"You selected: {query.data}, if you want to see the menu again please type '/menu'")
    elif query.data == "/lan":
        lan(update, context)
        query.edit_message_text(text=f"You selected: {query.data}, if you want to see the menu again please type '/menu'")
    elif query.data == "/blog":
        blog(update, context)
        query.edit_message_text(text=f"You selected: {query.data}, if you want to see the menu again please type '/menu'")
    elif query.data == "/contact":
        contact(update, context)
        query.edit_message_text(text=f"You selected: {query.data}, if you want to see the menu again please type '/menu'")
    elif query.data == "/id_fraud":
        id_fraud(update, context)
        #query.edit_message_text(text=f"You selected: {query.data}, type '/show_work_projects' if you want to see the projects menu again or go back to the main '/menu'")
    elif query.data == "/churn_pred":
        churn_pred(update, context)
        #query.edit_message_text(text=f"You selected: {query.data}, type '/show_work_projects' if you want to see the projects menu again or go back to the main '/menu'")
    elif query.data == "/disease_pred":
        disease_pred(update, context)
        #query.edit_message_text(text=f"You selected: {query.data}, type '/show_work_projects' if you want to see the projects menu again or go back to the main '/menu'")
    elif query.data == "/lstm":
        lstm(update, context)
        #query.edit_message_text(text=f"You selected: {query.data}, type '/show_work_projects' if you want to see the projects menu again or go back to the main '/menu'")
    #query.edit_message_text(text=f"You selected: {query.data}, if you want to see the menu again please type '/menu'")
    #query.edit_message_text(text=f"You selected: {queri.data}, if you want to see the projects again please type '/work_projects' or go back to the main '/menu'")

def show_work_projects(update: Update, context: CallbackContext) -> None:
    """Send Message on '/start'."""
    keyboard = [
        [
            InlineKeyboardButton("🆔 Fraud Prevention‍", callback_data="/id_fraud"),
            InlineKeyboardButton("📉 Churn Prediction‍", callback_data="/churn_pred")
        ],
        [
            InlineKeyboardButton("🧬‍ Disease Prediction", callback_data="/disease_pred"),
            InlineKeyboardButton("🏥 LSTM Agent", callback_data="/lstm"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("These are some of the projects I've worked on:", reply_markup=reply_markup)


def bio(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"I am Michelle, currently based in 🇨🇭 Switzerland holding a valid B permit. \n\n")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"I 🎓 as a Computer Scientist and I've been working on Machine Learning in areas such as Computer Vision and Natural Language Processing, designing and implementing state of the art algorithms which are nowadays impacting thousands of people in Latin America.")


def work_exp(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"My experience comprises projects like an alliance with Peru’s government in order to predict the population's most common diseases based on historical data, to the development and implementation of an ID fraud prevention system for Mexican ID cards.")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"If you want to know more ⬇\n\n /show_work_projects")


def per_project(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I run a Machine Learning non-profit community. We organize workshops and create content to teach fundamentals as well as advanced ML concepts and practices in order to help members to start, develop and apply models in real-life applications")
    context.bot.send_message(chat_id=update.effective_chat.id, text="We are currently +1100 members, join to the community in: 🌐 https://www.meetup.com/es/AI-Learners/")


def awards(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"• Selected as one of the 200 most qualified world Young Researchers to attend Heidelberg Laureate Forum in 🇩🇪\n"
                                                                    f"• 1st place FixIT Hackathon by Google, Mountain View, California, 🇺🇸\n"
                                                                    f"• 2nd place Robot Games Zero Latitude, Quito, 🇪🇨\n"
                                                                    f"• 1st place Hackathon FixIT UNAM, CDMX 🇲🇽\n"
                                                                    f"• M2X IoT award Hackathon AT&T, Guadalajara 🇲🇽\n"
                                                                    f"• 3rd place Startup Weekend Research Edition \n"
                                                                    f"• 4th place Mini Sumo Robogames, San Mateo, California, 🇺🇸\n"
                                                                    f"• Team Leader of the Piloto I-Corps of Mexico & United States Foundation for Science (FUMEC)\n"
                                                                    f"• Research and Development Director at Polytechnic Robotics Community")


def skills(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"• Data Cleaning, Visualization and Modeling 📊 \n"
                                                                    f"• Model development experience with TensorFlow, Keras, Spark and Scikit-learn\n"
                                                                    f"• Experience with Computer Vision tools such as YOLO, OpenCV and Tesseract\n"
                                                                    f"• Experience with visualizations tools such as Bokeh and Matplotlib\n"
                                                                    f"• Proficiency with Python 🐍\n"
                                                                    f"• Prior experience with Java ☕ and Javascript\n"
                                                                    f"• Experience in creating Docker containers 🐳 \n"
                                                                    f"• Experience with Frontend Development using HTML5, CSS, NodeJs")


def lan(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"🌕 My mother tongue is Spanish\n"
                                                                    f"🌖 I speak English fluently\n"
                                                                    f"🌗 I have a B1 German level")


def blog(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Since one of the things that I enjoy is to write and to share kwnoledge, I write in Medium about AI (only in spanish, for the moment)")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Here's the 🔗 to my blog: https://medium.com/@MichDiaz_/")


def contact(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="📧 Reach me out here:")
    context.bot.send_message(chat_id=update.effective_chat.id, text="lmo5ia@m.womenhack.com")
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://www.linkedin.com/in/michellediazdev/")


def helper(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="How can I help you?")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def error(update, context):
    logger.warning('Update {} caused error {}'.format(update, context.error))


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


def id_fraud(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"The standard process for a service contract (internet, tv subscription, etc.) in Mexico is to validate if the solicitor is a real person and registered in the national population registry through the solicitor’s ID. This validation process was made manually which led to process inefficiency and to clients’ discontent. Therefore, it was crucial to tackle this by fully automating the process.\n\n"
                                                                    f"My approach was to build a Mexican ID cards' data extraction, recognition, and classification pipeline applying state of the art Computer Vision algorithms.\n\n"
                                                                    f"The technologies I used were:\n"
                                                                    f"OpenCV, YOLO v.3, Tesseract, PostgreSQL, ImgLabel")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Type '/show_work_projects' if you want to know more or type '/menu' if you want to go back to main menu")


def churn_pred(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"A high profile company was undergoing through a high employees churn rate which incremented recruiting and training costs.\n\n"
                                                                    f"I drove descriptive, diagnostic, predictive and prescriptive analyses to detect churn trends and causes, and to understand and predict employees’ behaviour. Finally, I developed a logistic regression model for churn prediction based on historical data provided.\n\n"
                                                                    f"The technologies I used were:\n"
                                                                    f"Pandas, Scikit-learn, Seaborn")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Type '/show_work_projects' if you want to know more or type '/menu' if you want to go back to main menu")


def disease_pred(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"This project was a partnership whith the Ministry of Health of Peru, which aimed to be integrated to a telemedicine platform in order to help doctors to identify possible diseases in advance based on a given patient’s medical records.\n\n"
                                                                    f"I designed and implemented ML architecture for risk factors analysis for diseases prediction.\n\n"
                                                                    f"The technologies I used were:\n"
                                                                    f"Pandas, Scikit-learn, Matplotlib, PostgreSQL, Flask")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Type '/show_work_projects' if you want to know more or type '/menu' if you want to go back to main menu")


def lstm(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Pediatrics needed a way to handle with endless incoming messages from patients who reached them out asking common children health questions. Due to their busy schedule, they were unable to respond to all messages. Hence, I developed a conversational agent that could handle these frequent situations based on previous conversations.\n\n"
                                                                    f"This project was also my bachelor thesis. I was able to apply NLP techniques such as seq2seq (which consisted of two Recurrent Neural Networks LSTM encoder - decoder) to mitigate the lack of conversational context and built a seq2seq wrapper for training, evaluating, saving and restoring trained model.\n\n"
                                                                    f"The technologies I used were:\n"
                                                                    f"TensorFlow, Numpy, heroku, SQLite")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Type '/show_work_projects' if you want to know more or type '/menu' if you want to go back to main menu")


def main():
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # On different commands answer in telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("helper", helper))
    dp.add_handler(CommandHandler("unknown", unknown))
    dp.add_handler(CommandHandler("bio", bio))
    dp.add_handler(CommandHandler("work_exp", work_exp))
    dp.add_handler(CommandHandler("per_project", per_project))
    dp.add_handler(CommandHandler("awards", awards))
    dp.add_handler(CommandHandler("skills", skills))
    dp.add_handler(CommandHandler("lan", lan))
    dp.add_handler(CommandHandler("blog", blog))
    dp.add_handler(CommandHandler("contact", contact))
    dp.add_handler(CommandHandler("menu", menu))
    dp.add_handler(CommandHandler("show_work_projects", show_work_projects))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # On non command i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Log all errors
    dp.add_error_handler(error)

    # Start the bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook(URL + TOKEN)

    updater.idle()


if __name__ == '__main__':
    main()

# Changing from Polling to Webhooks
# Firstly, we will modify how the bot fetches new data.
# The python-telegram-bot script uses polling instead of webhooks to fetch new data.
# For simple testing purposes, polling is sufficient because it’s simple to implement.
# However, the disadvantage of polling is that it is inefficient and the data it fetches
# is always old and never real-time. This is because polling sends a request at a predetermined
# frequency to detect any changes in the data, meaning it constantly checks if the data is modified,
# instead of being “notified” when a change is made to the data.
#