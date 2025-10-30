package cmd

import (
	"motivational-messages/notification"

	"github.com/spf13/cobra"
)

var eodMsgCmd = &cobra.Command{
	Use:   "eod",
	Short: "Sends an end of day reminder notification",
	Long:  `Sends an end of day reminder notification to encourage wrapping up work and logging off`,
	Args:  cobra.NoArgs,
	Run: func(cmd *cobra.Command, args []string) {
		message := EODMsg

		notification.SendPushoverNotification(message)
	},
}
