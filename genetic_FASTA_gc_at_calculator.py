#nucleotide analysis in terms of GC or AT percentage
#Presenmtation of the program
print("Welcome to the nucleotide analysis program!")
print("\nThis program allows you to analyze the GC and AT content of nucleotide sequences in FASTA format.")
print("""\n In genetics, the percentage of Cytosine-Guanine (CG) and Adenine-Thymine 
    (AT) is fundamental for hybridization processes, the creation of PCR primers,
     and the development of molecular probes.""")


print("\nRemember that in genetics, a GC content of approximately 40 to 60% is recommended!")

#start of the overall loop
while True:

#Insertion of FASTA-type information

    print("How do you want to insert the FASTA-type information?")
    print("1. from a FASTA-format document (.txt, .fasta) on the PC")
    print("2. Manually (CtrlC + CtrlV)")

    opcion = input("Select an option (1 or 2): ")

    if opcion == "1":
        #Example of a FASTA file
        from pathlib import Path
        Carchivo = Path("D:/")

        #FASTA file filter
        def es_fasta(ruta):
            try:
                with open(ruta, encoding="utf-8-sig") as x:
                    for linea in x:
                        if linea.strip():
                            return linea.startswith(">") 
                    return False
            except (OSError, UnicodeDecodeError):
                return False
            
        #Search for all FASTA files
        extensiones = ["*.fasta", "*.fa", "*.fna", "*.txt"]
        archivos = []
        for exit in extensiones:
            archivos.extend(Carchivo.rglob(exit))

        if not archivos:
            print("No FASTA files found in the specified folder.")

        else:
            #Find the most recently modified FASTA file
            ultimo = max(archivos, key=lambda a: a.stat().st_mtime)

            respuesta = input(f"Use the most recently modified FASTA file {ultimo.name}? (y/n): ")

            if respuesta == "y":
                ruta = ultimo
            else:
                #List all FASTA files found
                print("FASTA files found:")
                archivos.sort(key=lambda a: a.stat().st_mtime, reverse=True)
                for i, archivo in enumerate(archivos, start=1):
                    print(f"{i}. {archivo.name}")
                eleccion = int(input("Select the number of the file to use: "))
                ruta = archivos[eleccion - 1]

        with open(ruta, "r") as f:
            texto = f.read()
            print (texto)

        while True:
            respuesta = input("Do you want to use this FASTA file? (y/n): ")
            if respuesta.lower() == "y":
                #GC vs AT % analysis

                def countSeq (texto):
                    #ignore the first line if it starts with '>'
                    if texto.startswith(">"):
                        texto = texto.split("\n", 1)[1]
                    count = len(texto)
                    print(f"Total number of nucleotides: {count}")
                    GCconteo = texto.count("G") + texto.count("C")
                    ATconteo = texto.count("A") + texto.count("T")
                    GCporcentaje = (GCconteo / count) * 100
                    ATporcentaje = (ATconteo / count) * 100
                    print(f"GC content: {GCporcentaje:.2f}%")
                    print(f"AT content: {ATporcentaje:.2f}%")
                countSeq(texto)
                break

            elif respuesta.lower() == "n":
                print("Please select another FASTA file.")
                # Repeat the file selection process
                archivos.sort(key=lambda a: a.stat().st_mtime, reverse=True)
                for i, archivo in enumerate(archivos, start=1):
                    print(f"{i}. {archivo.name}")
                eleccion = int(input("Select the number of the file to use: "))
                ruta = archivos[eleccion - 1]
                with open(ruta, "r") as f:
                    texto = f.read()
                    print (texto)
            else:
                print("Invalid response. Please enter 'y' or 'n'.")

    #Manual bonding process (IGNORAR)

    elif opcion == "2":
        print("Enter the FASTA code and write END on a new line to finish: ")
        lines = []
        while True:
            line = input()
            if line == "END":
                break
            lines.append(line)
        text = "\n".join(lines)
        print("Entered FASTA file:\n", text)

        def segundoconteo (text):
            #ignore the first line if it starts with '>'
            if text.startswith(">"):
                text = text.split("\n", 1)[1]
            count = len(text)
            print(f"Total number of nucleotides: {count}")
            GCconteo = text.count("G") + text.count("C")
            ATconteo = text.count("A") + text.count("T")
            GCporcentaje = (GCconteo / count) * 100
            ATporcentaje = (ATconteo / count) * 100
            print(f"GC content: {GCporcentaje:.2f}%")
            print(f"AT content: {ATporcentaje:.2f}%")

        segundoconteo(text)

    continuar = input("Do you want to analyze another sequence? (y/n): ")
    if continuar.lower() != "y":
        print("thank you for using the program. Goodbye!")
        break

