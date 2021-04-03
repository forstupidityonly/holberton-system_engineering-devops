# create a file
file { '~/.ssh/config':
  ensure  => file,
  content => 'Host ubuntu@34.74.125.88
              HostName ubuntu@34.74.125.88
              User ubuntu
              IdentyFile ~/.ssh/holberton
              PasswordAuthentication no',
}
