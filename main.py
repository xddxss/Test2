#!/usr/bin/env python3
"""
批量注册智能体 - 主入口
使用CFspider实现匿名IP和指纹伪装
"""

import argparse
import logging
from core.agent import BatchRegistrationAgent

def setup_logging():
    """配置日志"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('registration.log', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='批量注册智能体')
    parser.add_argument('--site', type=str, default='bb.com',
                       help='目标网站域名 (如 bb.com)')
    parser.add_argument('--count', type=int, default=10,
                       help='要注册的账号数量')
    parser.add_argument('--workers-url', type=str, 
                       default='https://your-cf-workers.workers.dev',
                       help='CFspider Workers地址')
    parser.add_argument('--uuid', type=str, 
                       help='CFspider UUID (可选，不填自动生成)')
    parser.add_argument('--headless', action='store_true', default=True,
                       help='无头模式 (默认开启)')
    parser.add_argument('--delay', type=float, default=5.0,
                       help='账号间延迟秒数')
    
    args = parser.parse_args()
    
    # 创建并运行智能体
    agent = BatchRegistrationAgent(
        target_site=args.site,
        num_accounts=args.count,
        cf_workers_url=args.workers_url,
        cf_uuid=args.uuid,
        headless=args.headless,
        delay_between_accounts=args.delay
    )
    
    # 执行批量注册
    agent.run()
    
    # 显示统计结果
    agent.print_summary()

if __name__ == "__main__":
    setup_logging()
    main()

