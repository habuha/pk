from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import random
import time

class FunApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.score = 0
        self.start_time = time.time()
        
    def build(self):
        # 设置窗口颜色
        Window.clearcolor = get_color_from_hex('#2E8B57')
        
        # 主布局
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # 标题
        title = Label(
            text='🎮 趣味小游戏 🎮',
            size_hint_y=None,
            height=80,
            font_size='24sp',
            color=get_color_from_hex('#FFD700')
        )
        main_layout.add_widget(title)
        
        # 分数显示
        self.score_label = Label(
            text=f'得分: {self.score}',
            size_hint_y=None,
            height=50,
            font_size='18sp',
            color=get_color_from_hex('#FFFFFF')
        )
        main_layout.add_widget(self.score_label)
        
        # 时间显示
        self.time_label = Label(
            text='时间: 0秒',
            size_hint_y=None,
            height=50,
            font_size='18sp',
            color=get_color_from_hex('#FFFFFF')
        )
        main_layout.add_widget(self.time_label)
        
        # 游戏说明
        instruction = Label(
            text='点击按钮获得随机分数！\n连续点击有惊喜哦～',
            size_hint_y=None,
            height=80,
            font_size='16sp',
            color=get_color_from_hex('#E6E6FA'),
            halign='center'
        )
        main_layout.add_widget(instruction)
        
        # 游戏按钮
        self.game_button = Button(
            text='🎯 点击我！',
            size_hint_y=None,
            height=100,
            background_color=get_color_from_hex('#FF6B6B'),
            color=get_color_from_hex('#FFFFFF'),
            font_size='20sp'
        )
        self.game_button.bind(on_press=self.on_button_press)
        main_layout.add_widget(self.game_button)
        
        # 重置按钮
        reset_button = Button(
            text='🔄 重置游戏',
            size_hint_y=None,
            height=60,
            background_color=get_color_from_hex('#4ECDC4'),
            color=get_color_from_hex('#FFFFFF'),
            font_size='16sp'
        )
        reset_button.bind(on_press=self.reset_game)
        main_layout.add_widget(reset_button)
        
        # 开始定时器更新
        self.update_timer()
        
        return main_layout
    
    def on_button_press(self, instance):
        # 随机分数
        points = random.randint(1, 10)
        
        # 连续点击奖励
        if self.score > 0 and self.score % 10 == 0:
            bonus = random.randint(5, 20)
            points += bonus
            self.show_popup(f'🎉 连续点击奖励！\n额外获得 {bonus} 分！')
        
        self.score += points
        self.score_label.text = f'得分: {self.score}'
        
        # 按钮动画效果
        instance.background_color = get_color_from_hex('#FF8C00')
        instance.text = f'+{points}分！'
        
        # 恢复按钮状态
        def restore_button():
            instance.background_color = get_color_from_hex('#FF6B6B')
            instance.text = '🎯 点击我！'
        
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: restore_button(), 0.5)
    
    def reset_game(self, instance):
        self.score = 0
        self.start_time = time.time()
        self.score_label.text = f'得分: {self.score}'
        self.time_label.text = '时间: 0秒'
        self.show_popup('🔄 游戏已重置！')
    
    def update_timer(self):
        elapsed = int(time.time() - self.start_time)
        self.time_label.text = f'时间: {elapsed}秒'
        
        # 每秒更新一次
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: self.update_timer(), 1.0)
    
    def show_popup(self, message):
        popup = Popup(
            title='提示',
            content=Label(text=message),
            size_hint=(None, None),
            size=(300, 200),
            background_color=get_color_from_hex('#4ECDC4')
        )
        popup.open()
        
        # 2秒后自动关闭
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: popup.dismiss(), 2.0)

if __name__ == '__main__':
    FunApp().run()
