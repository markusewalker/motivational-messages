package cmd

import (
	"os"

	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use:   "gomotivate",
	Short: "A CLI tool that provides motivational messages throughout the 9-5 workday",
	Long: `Motivational Messages is a CLI application that sends motivational messages at
specified times throughout the typical 9-5 workday`,
}

func Execute() {
	err := rootCmd.Execute()
	if err != nil {
		os.Exit(1)
	}
}

func init() {
	rootCmd.AddCommand(standupCmd)
	rootCmd.AddCommand(breakMsgCmd)
	rootCmd.AddCommand(lunchMsgCmd)
	rootCmd.AddCommand(eodMsgCmd)
}
