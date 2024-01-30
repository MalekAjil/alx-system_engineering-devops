#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method
arg = ARGV[0]
regex = /School/
  if regex.match(arg)
    puts "#{regex}"
end
