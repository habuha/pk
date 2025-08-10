#!/usr/bin/env python3
"""
本地测试脚本 - 在构建APK之前测试程序功能
"""

import sys
import os

def test_imports():
    """测试所有必要的导入"""
    print("🔍 测试导入...")
    
    try:
        import kivy
        print(f"✅ Kivy版本: {kivy.__version__}")
    except ImportError as e:
        print(f"❌ Kivy导入失败: {e}")
        return False
    
    try:
        from kivy.app import App
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.button import Button
        from kivy.uix.label import Label
        from kivy.uix.textinput import TextInput
        from kivy.uix.popup import Popup
        from kivy.core.window import Window
        from kivy.utils import get_color_from_hex
        print("✅ 所有Kivy组件导入成功")
    except ImportError as e:
        print(f"❌ Kivy组件导入失败: {e}")
        return False
    
    try:
        import random
        import time
        print("✅ 标准库导入成功")
    except ImportError as e:
        print(f"❌ 标准库导入失败: {e}")
        return False
    
    return True

def test_basic_functionality():
    """测试基本功能"""
    print("\n🔍 测试基本功能...")
    
    try:
        # 测试随机数生成
        rand_num = random.randint(1, 10)
        print(f"✅ 随机数生成: {rand_num}")
        
        # 测试时间功能
        current_time = time.time()
        print(f"✅ 时间功能: {current_time}")
        
        # 测试颜色转换
        color = get_color_from_hex('#FF0000')
        print(f"✅ 颜色转换: {color}")
        
        return True
    except Exception as e:
        print(f"❌ 基本功能测试失败: {e}")
        return False

def test_app_creation():
    """测试应用创建"""
    print("\n🔍 测试应用创建...")
    
    try:
        # 导入主应用
        from main import FunApp
        
        # 创建应用实例
        app = FunApp()
        print("✅ 应用实例创建成功")
        
        # 测试应用属性
        if hasattr(app, 'score'):
            print(f"✅ 应用属性检查: score = {app.score}")
        
        return True
    except Exception as e:
        print(f"❌ 应用创建测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("🚀 开始本地测试...\n")
    
    # 检查Python版本
    print(f"🐍 Python版本: {sys.version}")
    
    # 检查当前目录
    print(f"📁 当前目录: {os.getcwd()}")
    
    # 检查必要文件
    required_files = ['main.py', 'requirements.txt', 'buildozer.spec']
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ 文件存在: {file}")
        else:
            print(f"❌ 文件缺失: {file}")
    
    print("\n" + "="*50)
    
    # 运行测试
    tests = [
        test_imports,
        test_basic_functionality,
        test_app_creation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ 测试异常: {e}")
    
    print("\n" + "="*50)
    print(f"📊 测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！可以开始构建APK了")
        return True
    else:
        print("⚠️  部分测试失败，请检查问题后再构建APK")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
