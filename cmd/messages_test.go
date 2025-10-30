package cmd

import (
	"testing"
)

func getMessage(args []string, message string) string {
	if len(args) > 0 && args[0] != "" {
		return args[0]
	}

	return message
}

func TestGetStandupMessage(t *testing.T) {
	tests := []struct {
		args     []string
		expected string
	}{
		{[]string{}, StandupMsg},
		{[]string{"Bogus message"}, "Bogus message"},
	}
	for _, test := range tests {
		result := getMessage(test.args, StandupMsg)
		if result != test.expected {
			t.Errorf("getMessage(%v) == %v, want %v", test.args, result, test.expected)
		}
	}
}

func TestGetBreakMessage(t *testing.T) {
	tests := []struct {
		args     []string
		expected string
	}{
		{[]string{}, BreakMsg},
		{[]string{"Bogus message"}, "Bogus message"},
	}
	for _, test := range tests {
		result := getMessage(test.args, BreakMsg)
		if result != test.expected {
			t.Errorf("getMessage(%v) == %v, want %v", test.args, result, test.expected)
		}
	}
}

func TestGetLunchMessage(t *testing.T) {
	tests := []struct {
		args     []string
		expected string
	}{
		{[]string{}, LunchMsg},
		{[]string{"Bogus message"}, "Bogus message"},
	}
	for _, test := range tests {
		result := getMessage(test.args, LunchMsg)
		if result != test.expected {
			t.Errorf("getMessage(%v) == %v, want %v", test.args, result, test.expected)
		}
	}
}

func TestGetEndWorkMessage(t *testing.T) {
	tests := []struct {
		args     []string
		expected string
	}{
		{[]string{}, EODMsg},
		{[]string{"Bogus message"}, "Bogus message"},
	}
	for _, test := range tests {
		result := getMessage(test.args, EODMsg)
		if result != test.expected {
			t.Errorf("getMessage(%v) == %v, want %v", test.args, result, test.expected)
		}
	}
}
