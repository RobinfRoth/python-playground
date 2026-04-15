#!/usr/bin/env python3

from sys import getsizeof

class CompressedGene:
    bit_string: int

    def __init__(self, original_gene: str) -> None:
        self.bit_string = self._compress(original_gene)
    
    def _compress(self, original_gene: str) -> int:
        bit_string: int = 1
        for nucleotide in original_gene.upper():
            bit_string <<= 2
            match nucleotide:
                case "A":
                    bit_string |= 0b00
                case "C":
                    bit_string |= 0b01
                case "G":
                    bit_string |= 0b10
                case "T":
                    bit_string |= 0b11
                case any_value:
                    raise ValueError(f"Invalid nucleotide value '{any_value}'")

        return bit_string
    
    def decompress(self) -> str:
        gene_bit_string: int = self.bit_string
        decompressed_gene: list = []
        for _ in range(0, gene_bit_string.bit_length() - 1, 2):
            bit_value = gene_bit_string & 0b11

            match bit_value:
                case 0b00:
                    decompressed_gene.append("A")
                case 0b01:
                    decompressed_gene.append("C")
                case 0b10:
                    decompressed_gene.append("G")
                case 0b11:
                    decompressed_gene.append("T")
            
            gene_bit_string >>= 2

        return "".join(decompressed_gene[::-1])
    
    def __str__(self):
        return self.decompress()


if __name__ == "__main__":
    original: str = (
        "AACGTCGTTCCAGAACGTCGTTCCAGAACGTCGCTCCAGAACGTCGTTCCAGAACGAGTTTAGGAATCG"
        "GT" * 100
    )
    c_gene: CompressedGene = CompressedGene(original)

    size_original = getsizeof(original)
    size_compressed = getsizeof(c_gene.bit_string)
    print(f"Original Size: {size_original} Byte")
    print(f"Compressed Size: {size_compressed} Byte")
    print(f"Compression Ratio: {size_original / size_compressed}")
    print("Bit String: ", bit_string_pre_decompression := c_gene.bit_string)
    print("Decompressed Value: ", c_gene)

    assert original.upper() == c_gene.decompress(), ("Original gene and "
        "decompressed gene do not match."
    )
    assert bit_string_pre_decompression == c_gene.bit_string, ("Bit string is "
        "modified during decompression."
    )
