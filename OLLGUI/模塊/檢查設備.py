import platform
import subprocess
import sys
import os

def 是否为_mac系统():
    """通过平台模块检测是否为 macOS 系统"""
    return platform.system() == 'Darwin'

def 检查_windows下的苹果硬件():
    """在 Windows 上检查是否为 Mac 硬件"""
    try:
        # 检查系统制造商
        制造商 = subprocess.check_output(
            'wmic computersystem get manufacturer', 
            shell=True,
            stderr=subprocess.DEVNULL
        ).decode('utf-8', 'ignore')
        
        # 检查产品型号
        型号 = subprocess.check_output(
            'wmic computersystem get model',
            shell=True,
            stderr=subprocess.DEVNULL
        ).decode('utf-8', 'ignore')
        
        return 'Apple' in 制造商 or 'Mac' in 型号
    except Exception:
        return False

def 检查_bios中的苹果信息():
    """检查 BIOS 信息判断是否为 Mac 硬件"""
    try:
        结果 = subprocess.check_output(
            'wmic bios get manufacturer',
            shell=True,
            stderr=subprocess.DEVNULL
        ).decode('utf-8', 'ignore')
        return 'Apple' in 结果
    except Exception:
        return False

def 获取系统详情():
    """获取详细的系统信息"""
    系统类型 = platform.system()
    详细信息 = {
        '操作系统': 系统类型,
        '版本': platform.release(),
        '详细版本': platform.version(),
        '架构': platform.machine(),
        '处理器': platform.processor(),
        '是否为苹果设备': False,
        '硬件类型': '未知'
    }

    if 系统类型 == 'Darwin':
        详细信息.update({
            '是否为苹果设备': True,
            '硬件类型': '原生Mac',
            'macOS版本': platform.mac_ver()[0],
            '完整信息': f"macOS {platform.mac_ver()[0]} ({详细信息['版本']})"
        })
    elif 系统类型 == 'Windows':
        详细信息['完整信息'] = f"Windows {详细信息['版本']} ({详细信息['架构']})"
        
        # 检查是否是运行Windows的Mac设备
        if 检查_windows下的苹果硬件() or 检查_bios中的苹果信息():
            详细信息.update({
                '是否为苹果设备': True,
                '硬件类型': '运行Windows的Mac设备',
                '完整信息': f"Mac硬件运行Windows {详细信息['版本']}"
            })
    elif 系统类型 == 'Linux':
        详细信息['完整信息'] = f"Linux {详细信息['版本']} ({详细信息['架构']})"
        
        # 检查Hackintosh
        if os.path.exists('/sys/firmware/efi/efivars'):
            try:
                with open('/sys/firmware/efi/efivars/ApplePlatformInfo-8BE4DF61-93CA-11D2-AA0D-00E098032B8C', 'rb') as 文件:
                    if 文件.read(1):
                        详细信息.update({
                            '是否为苹果设备': True,
                            '硬件类型': 'Hackintosh',
                            '完整信息': f"Hackintosh运行Linux {详细信息['版本']}"
                        })
            except Exception:
                pass

    return 详细信息

def 打印详细报告(详细信息):
    """打印详细的检测报告"""
    print("\n=== 系统检测报告 ===")
    print(f"操作系统: {详细信息['操作系统']}")
    print(f"版本: {详细信息['版本']}")
    print(f"系统架构: {详细信息['架构']}")
    
    if 详细信息['操作系统'] == 'Darwin':
        print(f"macOS 版本: {详细信息.get('macOS版本', '未知')}")
    
    print(f"\n苹果设备检测结果: {'是' if 详细信息['是否为苹果设备'] else '否'}")
    
    if 详细信息['是否为苹果设备']:
        print(f"设备类型: {详细信息['硬件类型']}")
    
    print(f"\n完整系统信息: {详细信息['完整信息']}")

if __name__ == '__main__':
    系统详情 = 获取系统详情()
    打印详细报告(系统详情)
    
    # 返回适当的退出代码
    sys.exit(0 if 系统详情['是否为苹果设备'] else 1)