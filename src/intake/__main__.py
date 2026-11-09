import argparse
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def main():
    parser = argparse.ArgumentParser(description="Grok 新闻 webhook 与本地日报导出")
    sub = parser.add_subparsers(dest="command", required=True)
    serve = sub.add_parser("serve")
    serve.add_argument("--data-dir", default="data/grok-intake")
    serve.add_argument("--port", type=int, default=8787)
    serve.add_argument("--local-demo", action="store_true", help="无鉴权，仅限本机回环连接")
    serve.add_argument("--screenshot-mode", choices=["native-zh", "original"], default="original")
    serve.add_argument(
        "--legacy-screenshots", action="store_true", help="仅兼容旧入口；新双语入口不补截图"
    )
    serve.add_argument(
        "--telegram", action="store_true", help="显式启用真实 Telegram 发送，需配置 bot 和频道"
    )
    daily = sub.add_parser("digest", help="生成昨天08:00至今天08:00来稿的中英日报")
    daily.add_argument("--date", help="发布日期 YYYY-MM-DD；默认最近已到08:00的日期")
    daily.add_argument("--data-dir", default="data/grok-intake")
    daily.add_argument("--site", type=Path, default=Path("site"))
    export = sub.add_parser("export")
    export.add_argument(
        "--date", default=datetime.now(ZoneInfo("Asia/Shanghai")).date().isoformat()
    )
    export.add_argument("--data-dir", default="data/grok-intake")
    export.add_argument("--output", default="output/grok")
    export.add_argument("--site", type=Path, help="同步图文到本地 Astro site，不提交或推送")
    args = parser.parse_args()
    if args.command == "serve":
        import uvicorn
        from .app import create_app

        app = create_app(
            args.data_dir,
            local_demo=args.local_demo,
            mode=args.screenshot_mode,
            run_worker=args.legacy_screenshots,
            telegram=args.telegram,
        )
        # Bind loopback even in authenticated mode; production uses an HTTPS reverse proxy.
        uvicorn.run(app, host="127.0.0.1", port=args.port, proxy_headers=False, access_log=False)
    elif args.command == "digest":
        import json
        from .digest import build_digest
        from .store import Store

        directory = Path(args.data_dir).resolve()
        print(
            json.dumps(
                build_digest(Store(directory / "news.sqlite3"), directory, args.site, args.date),
                ensure_ascii=False,
            )
        )
    else:
        import json
        from .render import export_daily
        from .store import Store

        directory = Path(args.data_dir).resolve()
        print(
            json.dumps(
                export_daily(
                    Store(directory / "news.sqlite3"),
                    args.date,
                    directory,
                    Path(args.output),
                    args.site,
                ),
                ensure_ascii=False,
            )
        )


if __name__ == "__main__":
    main()
