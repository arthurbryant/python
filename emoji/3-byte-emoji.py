#!/usr/bin/env perl

foreach my $i (0xE0..0xEF) {
    foreach my $j (0x80..0xBF) {
        foreach my $k (0x80..0xBF) {
            # バイト列をUnicode(U)でパック
            print pack( 'U*', $i, $j, $k );
        }
    }
}
