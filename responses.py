from random import choice
import random


data = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": [
                "Hello",
                "Hi",
                "Greetings",
                "Sup",
                "What's up"
            ],
            "responses": [
                "Hello, agent! Ready for your next mission?",
                "Hi there! Looking for a team, or do you need game tips?",
                "Hey! How can I assist you in your Valorant or CS:GO endeavors today?"
            ]
        },
        # ... other intents ...
        {
            "tag": "goodbye",
            "patterns": [
                "Bye",
                "Goodbye",
                "See ya",
                "Catch you later"
            ],
            "responses": [
                "Goodbye! Remember, practice makes perfect.",
                "See you later! Don't forget to check back for game updates.",
                "Farewell! Stay sharp out there."
            ]
        },
        {
            "tag": "game_info",
            "patterns": [
                "Tell me about Valorant",
                "What is CS:GO",
                "Game modes in Valorant",
                "How to play CS:GO"
            ],
            "responses": [
                "Valorant is a team-based tactical shooter where precise aim and strategic skills are key to victory.",
                "CS:GO, or Counter-Strike: Global Offensive, is a competitive first-person shooter known for its intense gameplay and esports scene.",
                "Valorant has several game modes, including Unrated, Competitive, Spike Rush, and Deathmatch.",
                "In CS:GO, two teams, Terrorists and Counter-Terrorists, compete in game modes to complete objectives or eliminate the opposing team."
            ]
        },
        {
            "tag": "tips",
            "patterns": [
                "Any tips for Valorant?",
                "How to improve in CS:GO",
                "Best weapons in Valorant",
                "CS:GO strategies"
            ],
            "responses": [
                "Practice your aim daily, learn agent abilities, and communicate effectively with your team.",
                "Mastering spray patterns, map knowledge, and game sense are key to improving in CS:GO.",
                "In Valorant, weapons like the Vandal and Phantom are popular choices for their balanced damage and recoil.",
                "In CS:GO, successful strategies often involve controlling the map, using utility effectively, and teamwork."
            ]
        },
        {
            "tag": "matchmaking",
            "patterns": [
                "Looking for a Valorant team",
                "Need a CS:GO group",
                "How to find teammates",
                "Valorant team up"
            ],
            "responses": [
                "Check out the #team-up channel to find fellow Valorant players to squad up with!",
                "Post in #cs-go-group to connect with other CS:GO players looking for team members.",
                "You can find teammates by sharing your rank and preferred role in the dedicated channels!"
            ]
        },
        {
            "tag": "esports",
            "patterns": [
                "Upcoming Valorant tournaments",
                "CS:GO esports news",
                "Valorant competitive scene",
                "Who won the latest CS:GO tournament?"
            ],
            "responses": [
                "Stay tuned to the #valorant-tournaments channel for announcements and discussion about upcoming events!",
                "For the latest in CS:GO esports, check out the #csgo-news channel.",
                "The Valorant competitive scene is rapidly growing, with events ranging from community tournaments to the Valorant Champions Tour.",
                "The winner of the latest CS:GO tournament and match highlights can be found in the #tournament-results channel."
            ]
        },
        {
            "tag": "updates",
            "patterns": [
                "Latest Valorant update",
                "CS:GO patch notes",
                "New agents in Valorant",
                "CS:GO weapon balance changes"
            ],
            "responses": [
                "Check out the #valorant-updates channel for the latest game patches and agent news!",
                "Patch notes and weapon balance changes for CS:GO are posted in the #csgo-updates channel.",
                "New Valorant agents are discussed in #agent-reveal, including abilities and gameplay strategies.",
                "For detailed discussions on weapon balance and game mechanics changes in CS:GO, head over to #weapon-discussion."
            ]
        },
        {
            "tag": "jokes",
            "patterns": [
                "Tell me a Valorant joke",
                "CS:GO joke",
                "Make me laugh with a game joke"
            ],

            "responses": [
                "Why did the Valorant player apologize to the spike? Because he couldn't defuse the situation!",
                "How do CS:GO players stay fresh? They always switch sides halfway through!",
                "What do you call a Valorant agent who loves to garden? Sage!",
                "Why was the Counter-Terrorist bad at hide and seek? Because he always defused the hiding spot!"
            ]
        },
        {
            "tag": "technical_support",
            "patterns": [
                "Having trouble launching Valorant",
                "CS:GO crashes on startup",
                "Valorant network lag",
                "Fix for CS:GO audio issues"
            ],
            "responses": [
                "Make sure your graphics drivers are up to date and that Valorant is allowed through your firewall.",
                "For CS:GO crashes, verify the integrity of game files through Steam. Sometimes, outdated files cause issues.",
                "Experiencing network lag in Valorant? Check your internet connection and consider using a wired connection for better stability.",
                "Audio issues in CS:GO can often be fixed by changing audio settings in-game or ensuring your audio drivers are current."
            ]
        },
        {
            "tag": "community_events",
            "patterns": [
                "Valorant community tournaments",
                "CS:GO meetups",
                "Valorant fan art contest",
                "CS:GO community game nights"
            ],
            "responses": [
                "Join our community tournaments to showcase your Valorant skills and win prizes! Check #community-tournaments for more info.",
                "CS:GO meetups are a great way to connect with other players in your area. See #meetups for upcoming events.",
                "Share your creativity in the Valorant fan art contest and see how your art stacks up against others! Details in #fan-art-contest.",
                "Don't miss our CS:GO community game nights for fun and casual gameplay. Join the community on #game-night."
            ]
        },
        {
            "tag": "patch_notes_discussion",
            "patterns": [
                "Discuss Valorant patch notes",
                "Thoughts on the latest CS:GO update",
                "Valorant update analysis",
                "CS:GO patch review"
            ],
            "responses": [
                "Let's break down the latest Valorant patch notes. Join the discussion in #patch-notes-discussion!",
                "What does everyone think about the recent CS:GO update? Share your thoughts in #update-thoughts.",
                "Analyzing the latest Valorant update can reveal a lot about the future meta. Dive into the analysis with us in #update-analysis.",
                "Review the latest CS:GO patch with the community and share your insights in #patch-review."
            ]
        }
    ]
}

intent_dict = {intent["tag"]: {"patterns": intent["patterns"], "responses": intent["responses"]} for intent in data["intents"]}

def get_responses(user_message: str) -> str:
    for intent_tag, intent_data in intent_dict.items():
        for pattern in intent_data["patterns"]:
            if pattern.lower() in user_message.lower():
                return random.choice(intent_data["responses"])
    return "I'm not sure how to respond to that. Try asking about Valorant, CS:GO, or game tips."