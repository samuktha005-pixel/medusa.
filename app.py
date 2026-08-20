import random
from nicegui import ui

ui.label('Hello from NiceGUI on Android!')
# Set port explicitly 
ui.run(port=8080, host='127.0.0.1', reload=False)

# 1. Custom ocean-based styling and theme injection
ui.add_head_html("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;600;700&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
<style>
    :root {
        --bg-page: linear-gradient(180deg, #1b4965 0%, #001d3d 100%);
        --bg-card: rgba(255, 255, 255, 0.92);
        --bg-soft: rgba(255, 255, 255, 0.15);
        --blue: #2a9d8f; --blue-dark: #003049; --blue-mid: #457b9d;
        --coral: #e76f51; --amber: #f4a261; --green: #2a9d8f;
        --line: rgba(255, 255, 255, 0.2); --shadow: 0 10px 30px rgba(0,29,61,0.3);
    }
    body {
        margin: 0; font-family: 'Nunito', sans-serif;
        background: radial-gradient(circle at center, #1b4965 0%, #000814 100%);
        min-height: 100vh; display: flex; align-items: center; justify-content: center;
    }
    h1, h2, h3 { font-family: 'Baloo 2', cursive; color: var(--blue-dark); margin: 0; }
</style>
""")

# 2. ISL Curriculum Database (Complete A-Z & 1-10)
CATEGORIES = [
    {
        'id': 'greetings',
        'name': 'Greetings',
        'signs': [
            {'name': 'Hello', 'desc': 'Wave your open hand from side to side with a friendly expression.'},
            {'name': 'Thank you', 'desc': 'Touch fingertips to your chin, then move your hand forward towards the person.'},
            {'name': 'Please', 'desc': 'Rub an open palm in a circular motion on your chest.'},
            {'name': 'Sorry', 'desc': 'Make a fist and rub it in a circle on the center of your chest.'},
            {'name': 'Goodbye', 'desc': 'Open and close your fingers while raising your hand in a wave.'},
        ],
    },
    {
        'id': 'alphabets',
        'name': 'Alphabets (A-Z)',
        'signs': [
            {'name': 'A', 'desc': 'Join both thumbs together pointing upwards while resting other fingers in fists (ISL two-handed A).'},
            {'name': 'B', 'desc': 'Form two closed circles using thumb and index fingers on both hands touched together.'},
            {'name': 'C', 'desc': 'Form a curved "C" shape using your dominant thumb and curved fingers.'},
            {'name': 'D', 'desc': 'Index and thumb of left hand form a circle with right index finger touching the top.'},
            {'name': 'E', 'desc': 'Right index finger points directly to the left index finger tip.'},
            {'name': 'F', 'desc': 'Place middle finger of right hand over index finger of left hand.'},
            {'name': 'G', 'desc': 'Place both closed fists one on top of the other like grinding gears.'},
            {'name': 'H', 'desc': 'Swipe right flat palm across the left flat open palm.'},
            {'name': 'I', 'desc': 'Point the right index finger to the tip of the left middle finger.'},
            {'name': 'J', 'desc': 'Draw a "J" curve on the palm of the left hand using the right index finger.'},
            {'name': 'K', 'desc': 'Point right index finger upwards and tap against left crooked index finger.'},
            {'name': 'L', 'desc': 'Place right index finger perpendicular to left palm to form an "L" shape.'},
            {'name': 'M', 'desc': 'Place three fingers of right hand onto the left flat palm.'},
            {'name': 'N', 'desc': 'Place two fingers of right hand onto the left flat palm.'},
            {'name': 'O', 'desc': 'Form an "O" shape by joining tips of thumb and fingers on one or both hands.'},
            {'name': 'P', 'desc': 'Form a circle with thumb and index finger and tap against left index finger.'},
            {'name': 'Q', 'desc': 'Hook right index finger into left thumb/index circle.'},
            {'name': 'R', 'desc': 'Place curved right index finger onto the left palm.'},
            {'name': 'S', 'desc': 'Hook little fingers of both hands together.'},
            {'name': 'T', 'desc': 'Touch right index finger to the base of left palm/thumb.'},
            {'name': 'U', 'desc': 'Place two parallel fingers of right hand against left palm.'},
            {'name': 'V', 'desc': 'Form a "V" shape with index and middle fingers on left palm.'},
            {'name': 'W', 'desc': 'Interlock fingers of both hands pointing upwards to form a "W".'},
            {'name': 'X', 'desc': 'Cross index fingers of both hands to form an "X".'},
            {'name': 'Y', 'desc': 'Place thumb and little finger of right hand against left palm.'},
            {'name': 'Z', 'desc': 'Right palm rests against left palm at a right angle.'},
        ],
    },
    {
        'id': 'numbers',
        'name': 'Numbers (1-10)',
        'signs': [
            {'name': 'One', 'desc': 'Hold up one index finger with palm facing outward.'},
            {'name': 'Two', 'desc': 'Hold up index and middle fingers separated.'},
            {'name': 'Three', 'desc': 'Hold up thumb, index, and middle fingers.'},
            {'name': 'Four', 'desc': 'Hold up four fingers with thumb tucked into palm.'},
            {'name': 'Five', 'desc': 'Hold up an open hand with all five fingers spread.'},
            {'name': 'Six', 'desc': 'Hold up five fingers on one hand and thumb on the other.'},
            {'name': 'Seven', 'desc': 'Hold up five fingers on one hand and two fingers on the other.'},
            {'name': 'Eight', 'desc': 'Hold up five fingers on one hand and three fingers on the other.'},
            {'name': 'Nine', 'desc': 'Hold up five fingers on one hand and four fingers on the other.'},
            {'name': 'Ten', 'desc': 'Hold up both open hands with all ten fingers spread.'},
        ],
    },
]

CAT_ICONS = {'greetings': '👋', 'alphabets': '🔤', 'numbers': '🔢'}

# 3. Master Question Bank for Randomized Quizzes
ALL_QUIZ_QUESTIONS = [
    {'question': 'Which sign matches: "Wave your open hand from side to side"?', 'correct': 'Hello', 'wrong': ['Please', 'Sorry', 'Goodbye']},
    {'question': 'How do you perform the ISL sign for "Thank you"?', 'correct': 'Touch fingertips to chin, move forward', 'wrong': ['Wave hands rapidly', 'Rub a circle on your chest', 'Hold up index finger']},
    {'question': 'What gesture represents the number "One"?', 'correct': 'Hold up one index finger', 'wrong': ['Hold up an open hand', 'Hold up index and middle finger', 'Make a closed fist']},
    {'question': 'How do you sign the alphabet "C" in ISL?', 'correct': 'Form a curved "C" shape using thumb and fingers', 'wrong': ['Cross index fingers', 'Hook little fingers together', 'Point index finger to middle finger']},
    {'question': 'Which alphabet is signed by crossing index fingers to form an "X"?', 'correct': 'X', 'wrong': ['V', 'T', 'Z']},
    {'question': 'How do you sign the number "Five"?', 'correct': 'Hold up an open hand with all five fingers spread', 'wrong': ['Hold up four fingers', 'Hold up both open hands', 'Make a fist']},
    {'question': 'How is the letter "A" represented in two-handed ISL?', 'correct': 'Join both thumbs together pointing upwards', 'wrong': ['Form two closed circles', 'Swipe right palm across left', 'Draw an A on palm']},
    {'question': 'What does rubbing an open palm in a circle on your chest mean?', 'correct': 'Please', 'wrong': ['Sorry', 'Thank you', 'Goodbye']},
    {'question': 'How do you sign the number "Ten"?', 'correct': 'Hold up both open hands with all ten fingers spread', 'wrong': ['Hold up five fingers on one hand', 'Hold up index and thumb', 'Wave open palm']},
    {'question': 'Which alphabet sign involves interlocking fingers pointing upwards to form a "W"?', 'correct': 'W', 'wrong': ['M', 'V', 'U']},
    {'question': 'Which letter is signed by pointing the right index finger to the tip of the left middle finger?', 'correct': 'I', 'wrong': ['E', 'A', 'O']},
    {'question': 'How do you sign "Sorry" in ISL?', 'correct': 'Make a fist and rub it in a circle on your chest', 'wrong': ['Rub an open palm on your chest', 'Touch chin and move forward', 'Wave hand side to side']},
]

# 4. Global App State
state = {
    'user_name': 'Ocean Explorer',
    'points': 340,
    'streak': 7,
    'visited_signs': set(),
    'daily_goal': '10 mins',
    'bonus_claimed': False,
    'lesson_cat': 0,
    'lesson_idx': 0,
    'current_screen': 'loading',
    'quiz_questions': [],
    'quiz_idx': 0,
    'quiz_score': 0,
    'quiz_active': False,
    'quiz_feedback': '',
    'quiz_answered': False,
    'search_query': '',
}

# 5. Navigation & Logic Handlers
def set_screen(screen_name):
    state['current_screen'] = screen_name
    state['quiz_feedback'] = ''
    state['quiz_answered'] = False
    refresh_screen()

def mark_sign_visited(cat_idx, sign_idx):
    key = f"{cat_idx}-{sign_idx}"
    if key not in state['visited_signs']:
        state['visited_signs'].add(key)
        state['points'] += 5
        ui.notify('New sign learned! +5 Pts ⭐', color='positive', icon='school')

def open_lesson(cat_idx, sign_idx):
    state['lesson_cat'] = cat_idx
    state['lesson_idx'] = sign_idx
    mark_sign_visited(cat_idx, sign_idx)
    set_screen('lesson')

def change_lesson_index(direction):
    cat = CATEGORIES[state['lesson_cat']]
    state['lesson_idx'] = (state['lesson_idx'] + direction) % len(cat['signs'])
    mark_sign_visited(state['lesson_cat'], state['lesson_idx'])
    refresh_screen()

def start_quiz():
    selected_raw = random.sample(ALL_QUIZ_QUESTIONS, min(5, len(ALL_QUIZ_QUESTIONS)))
    randomized = []
    for item in selected_raw:
        options = [item['correct']] + item['wrong']
        random.shuffle(options)
        correct_idx = options.index(item['correct'])
        randomized.append({
            'question': item['question'],
            'options': options,
            'answer': correct_idx,
        })
    state['quiz_questions'] = randomized
    state['quiz_active'] = True
    state['quiz_idx'] = 0
    state['quiz_score'] = 0
    state['quiz_feedback'] = ''
    state['quiz_answered'] = False
    refresh_screen()

def submit_answer(selected_idx):
    if state['quiz_answered']:
        return
    q = state['quiz_questions'][state['quiz_idx']]
    state['quiz_answered'] = True
    if selected_idx == q['answer']:
        state['quiz_score'] += 1
        state['quiz_feedback'] = 'Correct! 🎉 (+10 Points)'
        state['points'] += 10
        ui.notify('Correct Answer!', color='positive', icon='check')
    else:
        correct_text = q['options'][q['answer']]
        state['quiz_feedback'] = f'Incorrect. Correct answer: {correct_text}'
        ui.notify('Not quite right!', color='negative', icon='close')
    refresh_screen()

def next_question():
    state['quiz_idx'] += 1
    state['quiz_feedback'] = ''
    state['quiz_answered'] = False
    refresh_screen()

def update_search(e):
    state['search_query'] = e.value.lower()
    refresh_screen()

def claim_daily_bonus():
    if not state['bonus_claimed']:
        state['points'] += 25
        state['streak'] += 1
        state['bonus_claimed'] = True
        ui.notify('Claimed +25 Points & +1 Streak!', color='positive', icon='stars')
        refresh_screen()

def update_user_name(e):
    new_name = e.value.strip()
    state['user_name'] = new_name if new_name else 'Ocean Explorer'

def set_daily_goal(goal_text):
    state['daily_goal'] = goal_text
    ui.notify(f'Daily Goal updated to {goal_text}', color='info', icon='timer')
    refresh_screen()

# 6. Main Phone Viewport Container
with ui.element('div').style(
    'width:375px; height:780px; background:linear-gradient(180deg, #1b4965 0%, #001d3d 100%); '
    'border-radius:40px; box-shadow:0 20px 50px rgba(0,0,0,0.5), 0 0 0 10px #030b16; '
    'position:relative; overflow:hidden; display:flex; flex-direction:column;'
):
    screen_container = ui.element('div').style(
        'position:absolute; inset:0; display:flex; flex-direction:column; '
        'padding:28px 22px 90px; overflow-y:auto;'
    )

    def refresh_screen():
        screen_container.clear()
        with screen_container:
            s = state['current_screen']

            # --- SCREEN 1: LOADING / WELCOME ---
            if s == 'loading':
                with ui.column().style('align-items:center; text-align:center; width:100%; margin-top:10px;'):
                    ui.image('brown.jpg').style(
                        'width:130px; height:130px; border-radius:50%; object-fit:cover; '
                        'border:3px solid rgba(255,255,255,0.4); margin-top:10px; '
                        'box-shadow:0 8px 20px rgba(0,0,0,0.2);'
                    )
                    ui.label('Helo i am Blup!').style('font-family:"Baloo 2"; font-size:22px; color:white; margin-top:14px;')
                    ui.label('I will help you to learn ISL.').style('color:#90e0ef; font-size:13px; margin-top:4px;')

                with ui.row().style('display:flex; justify-content:space-around; margin-top:24px; width:100%;'):
                    for icon, label in [('🌊', 'Flow'), ('📔', 'Learn'), ('🌐', 'Connect')]:
                        with ui.card().style('background:rgba(255,255,255,0.1); border-radius:14px; padding:12px; text-align:center; flex:1; border:none;'):
                            ui.label(icon).style('font-size:20px;')
                            ui.label(label).style('color:white; font-size:11px; margin-top:4px;')

                ui.button('Start Exploring', on_click=lambda: set_screen('home')).classes('w-full').style(
                    'background:#48cae4; color:#030b16; font-weight:700; border-radius:16px; margin-top:auto; height:46px;'
                )

            # --- SCREEN 2: HOME (Current Reef section removed) ---
            elif s == 'home':
                ui.label(f"Welcome back, {state['user_name']}! 🌊").style('color:#90e0ef; font-size:13px;')
                ui.label('Ready to ride the tide?').style('font-family:"Baloo 2"; font-size:22px; color:white;')

                ui.label('Ocean Categories').style('font-weight:700; color:white; margin-top:24px; font-size:16px;')
                with ui.grid(columns=3).style('gap:10px; margin-top:12px; width:100%;'):
                    for idx, cat in enumerate(CATEGORIES):
                        icon = CAT_ICONS.get(cat['id'], '📖')
                        with ui.button(on_click=lambda i=idx: open_lesson(i, 0)).style(
                            'background:rgba(255,255,255,0.92); border-radius:18px; padding:18px 8px; '
                            'text-align:center; height:auto; box-shadow:0 4px 12px rgba(0,0,0,0.1); '
                            'display:flex; flex-direction:column; align-items:center;'
                        ).classes('w-full'):
                            ui.label(icon).style('font-size:26px;')
                            ui.label(cat['name']).style('font-size:12px; font-weight:700; color:var(--blue-dark); margin-top:6px;')
                            ui.label(f"{len(cat['signs'])} signs").style('font-size:10px; color:var(--blue-mid); margin-top:2px;')

            # --- SCREEN 3: LEARN / DICTIONARY ---
            elif s == 'learn':
                ui.label('Sign Library').style('font-family:"Baloo 2"; font-size:20px; color:white; margin-bottom:12px;')
                ui.input(placeholder='Search signs...', value=state['search_query'], on_change=update_search).style(
                    'width:100%; border-radius:14px; background:rgba(255,255,255,0.9);'
                ).props('outlined dense clearable')

                with ui.column().style('gap:10px; margin-top:14px; width:100%;'):
                    for cat_idx, cat in enumerate(CATEGORIES):
                        matching_signs = [
                            sign for sign in cat['signs']
                            if state['search_query'] in sign['name'].lower() or state['search_query'] in sign['desc'].lower()
                        ]
                        if not matching_signs and state['search_query']:
                            continue

                        icon = CAT_ICONS.get(cat['id'], '📖')
                        with ui.button(on_click=lambda i=cat_idx: open_lesson(i, 0)).style(
                            'background:rgba(255,255,255,0.92); border-radius:16px; padding:14px 16px; '
                            'width:100%; text-align:left; justify-content:space-between; box-shadow:0 4px 12px rgba(0,0,0,0.1);'
                        ).classes('w-full'):
                            with ui.row().style('align-items:center; width:100%; justify-content:space-between;'):
                                with ui.row().style('align-items:center; gap:14px;'):
                                    ui.label(icon).style('font-size:20px;')
                                    with ui.column().style('gap:0px;'):
                                        ui.label(cat['name']).style('font-weight:700; font-size:14.5px; color:var(--blue-dark);')
                                        ui.label(f"{len(matching_signs)} signs available").style('font-size:12px; color:var(--blue-mid);')
                                ui.label('›').style('color:var(--blue-mid); font-size:18px; font-weight:700;')

            # --- SCREEN 4: LESSON DETAIL ---
            elif s == 'lesson':
                cat = CATEGORIES[state['lesson_cat']]
                sign = cat['signs'][state['lesson_idx']]

                ui.button('← Back to Library', on_click=lambda: set_screen('learn')).style(
                    'background:transparent; border:1.5px solid rgba(255,255,255,0.4); color:white; border-radius:14px;'
                )
                ui.label(f"{cat['name']} ({state['lesson_idx'] + 1}/{len(cat['signs'])})").style(
                    'text-align:center; color:#90e0ef; margin-top:10px; font-size:13px; width:100%;'
                )

                with ui.card().style('background:rgba(255,255,255,0.95); border-radius:20px; padding:32px 20px; text-align:center; margin-top:14px; width:100%; box-shadow:var(--shadow);'):
                    ui.label(sign['name']).style('font-family:"Baloo 2"; font-size:32px; color:var(--blue-dark);')
                    ui.label(sign['desc']).style('color:var(--blue-mid); margin-top:14px; font-size:14.5px; line-height:1.5; font-weight:600;')

                with ui.row().style('display:flex; justify-content:space-between; margin-top:20px; align-items:center; width:100%;'):
                    ui.button('← Prev', on_click=lambda: change_lesson_index(-1)).style(
                        'border-radius:14px; background:rgba(255,255,255,0.2); color:white;'
                    )
                    ui.button('📷 Practice Cam', on_click=lambda: ui.notify('Webcam integration ready for AI verification!', icon='videocam')).style(
                        'border-radius:16px; padding:0 18px; height:44px; background:#48cae4; color:#030b16; font-weight:700;'
                    )
                    ui.button('Next →', on_click=lambda: change_lesson_index(1)).style(
                        'border-radius:14px; background:rgba(255,255,255,0.2); color:white;'
                    )

            # --- SCREEN 5: PRACTICE / QUIZ ---
            elif s == 'practice':
                ui.label('Reef Challenge 🏆').style('font-family:"Baloo 2"; font-size:20px; color:white; margin-bottom:12px;')

                if not state['quiz_active']:
                    with ui.card().style('background:rgba(255,255,255,0.95); border-radius:20px; padding:26px 20px; text-align:center; width:100%; box-shadow:var(--shadow);'):
                        ui.label('🌊').style('font-size:42px;')
                        ui.label('Test Your Skills').style('font-family:"Baloo 2"; font-size:18px; color:var(--blue-dark); margin-top:6px;')
                        ui.label('Every quiz is randomly shuffled from greetings, A–Z alphabets, and numbers!').style('color:var(--blue-mid); font-size:13px; margin:6px 0 16px;')
                        ui.button('Start Randomized Quiz', on_click=start_quiz).style(
                            'background:#48cae4; color:#030b16; font-weight:700; width:100%; border-radius:16px; height:46px;'
                        )
                else:
                    total_q = len(state['quiz_questions'])
                    if state['quiz_idx'] < total_q:
                        q = state['quiz_questions'][state['quiz_idx']]
                        with ui.card().style('background:rgba(255,255,255,0.95); border-radius:20px; padding:20px; width:100%; box-shadow:var(--shadow);'):
                            ui.label(f"Question {state['quiz_idx'] + 1} of {total_q}").style('color:var(--blue-mid); font-size:11px; font-weight:700;')
                            ui.label(q['question']).style('font-family:"Baloo 2"; font-size:16px; color:var(--blue-dark); margin:8px 0 14px;')

                            with ui.column().style('gap:8px; width:100%;'):
                                for idx, opt in enumerate(q['options']):
                                    btn_color = '#f1f5f9'
                                    text_color = 'var(--blue-dark)'
                                    if state['quiz_answered']:
                                        if idx == q['answer']:
                                            btn_color = '#d8f3dc'
                                            text_color = '#1b4332'
                                    
                                    ui.button(opt, on_click=lambda i=idx: submit_answer(i)).style(
                                        f'width:100%; background:{btn_color}; color:{text_color}; border-radius:12px; '
                                        'justify-content:flex-start; padding-left:14px; font-weight:600;'
                                    ).props('flat')

                            if state['quiz_feedback']:
                                is_correct = 'Correct' in state['quiz_feedback']
                                feedback_color = '#2a9d8f' if is_correct else '#e76f51'
                                ui.label(state['quiz_feedback']).style(
                                    f'margin-top:10px; font-weight:700; font-size:13px; color:{feedback_color};'
                                )
                                btn_label = 'Next Question →' if state['quiz_idx'] < total_q - 1 else 'See Results 🏆'
                                ui.button(btn_label, on_click=next_question).style(
                                    'margin-top:12px; background:var(--blue-dark); color:white; width:100%; border-radius:12px;'
                                )
                    else:
                        with ui.card().style('background:rgba(255,255,255,0.95); border-radius:20px; padding:26px 20px; text-align:center; width:100%; box-shadow:var(--shadow);'):
                            ui.label('🎉').style('font-size:45px;')
                            ui.label('Quiz Completed!').style('font-family:"Baloo 2"; font-size:20px; color:var(--blue-dark); margin-top:6px;')
                            ui.label(
                                f"You scored {state['quiz_score']} out of {total_q}!"
                            ).style('color:var(--blue-mid); font-size:13px; margin:6px 0 16px;')
                            ui.button('New Randomized Quiz', on_click=start_quiz).style(
                                'background:#48cae4; color:#030b16; font-weight:700; width:100%; border-radius:16px; height:46px;'
                            )

            # --- SCREEN 6: FUNCTIONAL PROFILE ---
            elif s == 'profile':
                with ui.column().style('align-items:center; text-align:center; width:100%;'):
                    ui.image('brown.jpg').style(
                        'width:86px; height:86px; border-radius:50%; object-fit:cover; '
                        'border:3px solid white; box-shadow:0 6px 15px rgba(0,0,0,0.2);'
                    )
                    
                    ui.label(f"{state['user_name']} 🌊").style('font-family:"Baloo 2"; font-size:20px; color:white; margin-top:8px;')
                    ui.label('Signed up for success').style('color:#90e0ef; font-size:12px;')

                    # Dynamic Stats Cards (Updated in real-time)
                    with ui.row().style('gap:8px; margin-top:14px; width:100%;'):
                        for num, label in [
                            (len(state['visited_signs']), 'Lessons'),
                            (state['points'], 'Points'),
                            (state['streak'], 'Streak'),
                        ]:
                            with ui.card().style('flex:1; background:rgba(255,255,255,0.92); border-radius:16px; text-align:center; padding:12px 4px; box-shadow:0 4px 12px rgba(0,0,0,0.1);'):
                                ui.label(str(num)).style('font-family:"Baloo 2"; font-size:19px; color:var(--blue-dark);')
                                ui.label(label).style('font-size:10px; color:var(--blue-mid); font-weight:700;')

                    # Functional Username Change Card
                    with ui.card().style('background:rgba(255,255,255,0.92); border-radius:16px; margin-top:12px; width:100%; padding:14px; text-align:left; box-shadow:0 4px 12px rgba(0,0,0,0.1);'):
                        ui.label('Profile Settings').style('font-weight:700; color:var(--blue-dark); font-size:13.5px;')
                        ui.input(
                            label='Display Name',
                            value=state['user_name'],
                            on_change=update_user_name
                        ).style('width:100%; margin-top:4px;').props('dense outlined')

                    # Functional Daily Goal Settings
                    with ui.card().style('background:rgba(255,255,255,0.92); border-radius:16px; margin-top:12px; width:100%; padding:14px; text-align:left; box-shadow:0 4px 12px rgba(0,0,0,0.1);'):
                        ui.label('Daily Learning Goal').style('font-weight:700; color:var(--blue-dark); font-size:13.5px;')
                        with ui.row().style('width:100%; justify-content:space-between; margin-top:8px;'):
                            for goal in ['5 mins', '10 mins', '20 mins']:
                                is_active = state['daily_goal'] == goal
                                bg = '#003049' if is_active else '#e0f1f8'
                                color = 'white' if is_active else '#003049'
                                ui.button(goal, on_click=lambda g=goal: set_daily_goal(g)).style(
                                    f'background:{bg}; color:{color}; border-radius:10px; font-size:11px; font-weight:700; padding:4px 10px; height:auto;'
                                ).props('flat')

                    # Claim Daily Reward Button
                    reward_text = 'Claimed Today (Check Back Tomorrow)' if state['bonus_claimed'] else '🎁 Claim Daily Bonus (+25 Pts)'
                    reward_bg = '#8d99ae' if state['bonus_claimed'] else '#48cae4'
                    ui.button(reward_text, on_click=claim_daily_bonus).style(
                        f'width:100%; background:{reward_bg}; color:#030b16; font-weight:700; border-radius:14px; margin-top:12px; height:44px;'
                    )

    # 6. Bottom Navigation Toolbar
    with ui.element('div').style(
        'position:absolute; left:0; right:0; bottom:0; background:rgba(3,11,22,0.85); '
        'backdrop-filter:blur(10px); border-top:1px solid rgba(255,255,255,0.1); '
        'display:flex; padding:10px 8px 16px; z-index:20;'
    ):
        for target, label in [
            ('home', 'Home'),
            ('learn', 'Learn'),
            ('practice', 'Practice'),
            ('profile', 'Profile'),
        ]:
            ui.button(label, on_click=lambda t=target: set_screen(t)).style(
                'flex:1; background:none; color:#90e0ef; font-family:"Nunito"; font-size:11px; font-weight:700;'
            ).props('flat')

# Initial app render
refresh_screen()

ui.run(port=8080, title='BLUP — Sea Theme ISL Learning App', reload=False)