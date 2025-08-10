#!/usr/bin/env python3
"""
本地运行脚本 - 在桌面环境测试游戏
"""

import sys
import os

def main():
    """主函数"""
    print("🎮 趣味小游戏 - 本地测试版")
    print("=" * 40)
    
    try:
        # 检查依赖
        print("🔍 检查依赖...")
        import kivy
        print(f"✅ Kivy {kivy.__version__} 已安装")
        
        # 导入并运行应用
        print("🚀 启动游戏...")
        from main import FunApp
        
        # 设置窗口大小（桌面环境）
        from kivy.core.window import Window
        Window.size = (400, 600)
        Window.minimum_width = 300
        Window.minimum_height = 500
        
        print("✅ 游戏启动成功！")
        print("💡 提示：点击按钮获得分数，连续点击有奖励！")
        
        # 运行应用
        FunApp().run()
        
    except ImportError as e:
        print(f"❌ 依赖缺失: {e}")
        print("\n🔧 解决方案:")
        print("1. 安装依赖: pip install -r requirements.txt")
        print("2. 或者: pip install kivy")
        return 1
        
    except Exception as e:
        print(f"❌ 运行错误: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
