import argparse

from utils.fetch_data import update_lotto_data
from utils.lotto_model import train_model
from utils.to_result import predict_numbers, send_slack


def build_parser():
    parser = argparse.ArgumentParser(description="Lotto project entrypoint")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("train", help="Train the lotto model")
    subparsers.add_parser("predict", help="Predict lotto numbers")
    subparsers.add_parser("update-data", help="Fetch and append the latest lotto draw")

    notify_parser = subparsers.add_parser("notify", help="Send a Slack message")
    notify_parser.add_argument("message", help="Slack message text")
    notify_parser.add_argument(
        "--slack-url",
        dest="slack_url",
        help="Slack webhook URL. Defaults to SLACK_URL env var.",
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "train":
        loss = train_model()
        print(f"training complete: loss={loss:.6f}")
    elif args.command == "predict":
        numbers = predict_numbers()
        print("predicted numbers:", numbers)
    elif args.command == "update-data":
        update_lotto_data()
        print("lotto data updated")
    elif args.command == "notify":
        send_slack(args.message, slack_url=args.slack_url)
        print("slack message sent")
    else:
        parser.error(f"unsupported command: {args.command}")


if __name__ == "__main__":
    main()
