import multiprocessing
import math
import time
from rich.progress import Progress
from rich.console import Console

def burn_cpu():
    while True:
        # 高耗能運算，讓 CPU 滿載
        x = 0.0001
        for _ in range(10000):
            x = math.sin(math.sqrt(x)) ** 2

def run_cpu_burner():
    # 建立 Console 物件，讓終端能顯示顏色與動畫
    console = Console()
    num_cores = multiprocessing.cpu_count()
    console.print(f"🚀 啟動 {num_cores} 核心來讓 CPU 滿載！", style="bold green")

    # 設置動畫
    with Progress() as progress:
        task = progress.add_task("[cyan]CPU 滿載中...", total=num_cores)
        
        processes = []
        for _ in range(num_cores):
            p = multiprocessing.Process(target=burn_cpu)
            p.start()
            processes.append(p)
            progress.update(task, advance=1)  # 每啟動一個核心，進度條更新

        try:
            while True:
                time.sleep(1)  # 維持滿載狀態
        except KeyboardInterrupt:
            console.print("\n🛑 停止 CPU 滿載測試！")
            for p in processes:
                p.terminate()

if __name__ == "__main__":
    run_cpu_burner()
