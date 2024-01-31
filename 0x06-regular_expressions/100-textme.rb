#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method
sender = ARGV[0].scan(/\[?from:(.*?)\]/).join
reciever = ARGV[0].scan(/\[to:(.+?)\]/).join
flags = ARGV[0].scan(/\[flags:(.+?)\]/).join
puts "#{sender},#{reciever},#{flags}"
