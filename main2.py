# Сделать так, чтобы приветствие менялось в зависимости от времени суток:
# • 6:00–12:00 → “Доброе утро, [имя]!” 
# • 12:00–18:00 → “Добрый день, [имя]!” 
# • 18:00–24:00 → “Добрый вечер, [имя]!” 
# • 0:00–6:00 → “Доброй ночи, [имя]!”

import flet as ft
import datetime 

def main(page: ft.Page):
    page.title = 'My first app'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text('Hello, world!')

    greeting_history = []
    history_text = ft.Text('Welcoming history:', style='bodyMedium')

    def on_button_click(e):
        name = name_input.value.strip()

        if name:
            current_hour = datetime.datetime.now().hour
            if 6 <= current_hour < 12:
                greeting_text.value = f'Good morning, {name}!'
            elif 12 <= current_hour < 18:
                greeting_text.value = f'Good afternoon, {name}!'
            elif 18 <= current_hour < 24:
                greeting_text.value = f'Good evening, {name}!'
            else:
                greeting_text.value = f'Good night, {name}!'
            greet_button.text = 'Click me again!'
            name_input.value = ''

            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            greeting_history.append(f'{name} at {current_time}')

            history_text.value = 'Welcoming history:\n' + '\n'.join(greeting_history)
        else:
            greeting_text.value = 'Please enter your name!'

        page.update()

    name_input = ft.TextField(label='Enter your name', autofocus=True, on_submit=on_button_click)

    def clear_history(e):
        greeting_history.clear()
        history_text.value = 'Welcoming history:'
        page.update()

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()



    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, tooltip="Theme change", on_click=toggle_theme)

    clear_button = ft.ElevatedButton('Clear history', on_click=clear_history)

    clear_button_icon = ft.IconButton(icon=ft.icons.CLEAR, tooltip="Clear history", on_click=clear_history)
        
    greet_button = ft.ElevatedButton('Click me!', on_click=on_button_click)

    page.add(ft.Row([theme_button,clear_button, clear_button_icon],
            alignment=ft.MainAxisAlignment.CENTER),    
            greeting_text,
            name_input,
            greet_button,
            history_text,
    )

ft.app(target=main)

# ft.app(target=main, view=ft.WEB_BROWSER)
