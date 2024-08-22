/*NOME: PEDRO FERNANDO WIEZEL
CURSO: ADS
*/

package main;

import interfaceUsuario.InterfaceUsuario;
import financiamento.Financiamento;
import financiamento.Casa;
import financiamento.Apartamento;
import financiamento.Terreno;
import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Locale;

/*Professor, esse método main ficou gigantesco porque eu não consegui implementar os métodos de ler caracteres,
salvar serializáveis, etc., de um outro modo. Eu acredito que há um modo melhor que planejo estudar, mas por enquanto,
os métodos de salvar tudo e ler tudo estão aqui nesse arquivo.

Outra coisa é que na primeira vez que ele rodar ele vai acusar que o .dat não existe, mas depois disso funciona normalmente
porque, evidentemente, o arquivo será criado.
*/

public class Main {

    private static ArrayList<Financiamento> listadefinanciamentos = new ArrayList<Financiamento>();

    public static void main(String[] args) {
        Scanner coletor = new Scanner(System.in);
        coletor.useLocale(Locale.forLanguageTag("pt-BR"));

        lerSerializavelDados();

        System.out.println("Bem vindo ao simulador de financiamentos: ");

        Casa casa = new Casa(500000, 10, 10, 200, 150);
        listadefinanciamentos.add(casa);
        Casa casa2 = new Casa(3000000, 30, 5, 400, 200);
        listadefinanciamentos.add(casa2);
        Apartamento ap = new Apartamento(500000, 10, 10, 15, 2);
        listadefinanciamentos.add(ap);
        Terreno terreno1 = new Terreno(6500000, 5, 20, "RESIDENCIAL");
        listadefinanciamentos.add(terreno1);

        int tipoFinanciamento = 0; //1 = Casa; 2 = Apartamento; 3 = Terreno

        for (int n = 1; n <= 1; n++) {

            System.out.println(new String(new char[50]).replace("\0", "\r\n"));
            /*código que encontrei online para "limpar" o terminal*/

            System.out.println("Preparando financiamento do usuário (os outros estão hardcodados)...");

            double valorImovel = InterfaceUsuario.coletar_valor_imovel();
            int prazoFinanciamento = InterfaceUsuario.coletar_prazo_financiamento();
            double taxaJurosAnual = InterfaceUsuario.coletar_taxa_juros_anual();

            boolean entradaValida = false;
            do {
                try {
                    System.out.println("Qual tipo de financiamento deseja fazer com esses dados?");
                    System.out.println("1 - Casa; 2 - Apartamento; 3 - Terreno");
                    tipoFinanciamento = Integer.parseInt(coletor.nextLine());
                    if (tipoFinanciamento < 1 || tipoFinanciamento > 3) {
                        throw new IllegalArgumentException("Escolha uma opção entre 1, 2 ou 3.");
                    }
                    entradaValida = true;
                } catch (NumberFormatException e) {
                    System.out.println("Por favor, digite um valor numérico válido.");
                } catch (IllegalArgumentException e) {
                    System.out.println(e.getMessage());
                }
            } while (!entradaValida);

            if (tipoFinanciamento == 1) {
                double tamanhoTerreno = InterfaceUsuario.coletarTamanhoTerreno();
                double tamanhoConstruido = InterfaceUsuario.coletarTamanhoConstruido();
                Casa novacasa = new Casa(valorImovel, prazoFinanciamento, taxaJurosAnual, tamanhoTerreno, tamanhoConstruido);
                casa.setTamanhoTerreno(tamanhoTerreno);
                casa.setTamanhoAreaConstruida(tamanhoConstruido);
                listadefinanciamentos.add(novacasa);
            } else if (tipoFinanciamento == 2) {
                int andar = InterfaceUsuario.coletarAndarApartamento();
                int numeroVagas = InterfaceUsuario.coletarNumeroVagasGaragem();
                Apartamento apartamento = new Apartamento(valorImovel, prazoFinanciamento, taxaJurosAnual, andar, numeroVagas);
                apartamento.setNumeroAndar(andar);
                apartamento.setNumeroVagasGaragem(numeroVagas);
                listadefinanciamentos.add(apartamento);
            } else if (tipoFinanciamento == 3) {
                String zona = InterfaceUsuario.coletarZona();
                Terreno terreno = new Terreno(valorImovel, prazoFinanciamento, taxaJurosAnual, zona);
                terreno.setZona(zona);
                listadefinanciamentos.add(terreno);
            }
        }

        double somaValoresFinanciamentos = 0;
        double somaValoresImoveis = 0;
        for (int i = 0; i < listadefinanciamentos.size(); i++) {
            somaValoresImoveis += listadefinanciamentos.get(i).getValorImovel();
            somaValoresFinanciamentos += listadefinanciamentos.get(i).calcular_total_pagamento();
        }
        System.out.println("-------------------");
        System.out.println("Valor total dos imóveis: " + somaValoresImoveis);
        System.out.println("Valor total dos financiamentos: " + somaValoresFinanciamentos);
        System.out.println("-------------------");

        escreverCaracteres();
        lerCaracteres();
        salvarSerializavelDados();

    }

    public static void escreverCaracteres () {
        String texto = "";
        FileWriter out = null;
        int contagemLetra = 0;
        System.out.println("\nSalvando dados em .txt...");
        try {
            out = new FileWriter("dadosFinanciamentos.txt");
            for (Financiamento fin : listadefinanciamentos){
                texto = texto + fin.imprimir_dados_financiamento();
            }
            while (contagemLetra < texto.length()){
                out.write(texto.charAt(contagemLetra));
                contagemLetra++;
            }
            out.close();
        } catch(FileNotFoundException e){
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void lerCaracteres(){
        FileReader in = null;
        System.out.println(("\nDados do arquivo de financiamentos em .txt: \n"));
        try {
            in = new FileReader(("dadosFinanciamentos.txt"));
            int c;
            while ((c = in.read()) != -1)
                System.out.print((char) c);
            in.close();
        } catch(FileNotFoundException e){
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void salvarSerializavelDados(){
        ObjectOutputStream outputStream = null;
        try{
            outputStream = new ObjectOutputStream(new FileOutputStream("dadosFinanciamentos.dat"));
            for (Financiamento fin : listadefinanciamentos){
                outputStream.writeObject(fin);
            }
        } catch (FileNotFoundException ex){
            ex.printStackTrace();
        } catch (IOException ex){
            ex.printStackTrace();
        } finally {
            try{
                if(outputStream != null){
                    outputStream.flush();
                    outputStream.close();
                }
            } catch (IOException ex){
                ex.printStackTrace();
            }
        }
    }

    public static void lerSerializavelDados() {
        ObjectInputStream inputStream = null;
        try{
            inputStream = new ObjectInputStream(new FileInputStream("dadosfinanciamentos.dat"));
            Object obj = null;
            while ((obj = inputStream.readObject()) != null) {
                if (obj instanceof Casa){
                    listadefinanciamentos.add((Casa) obj);
                }
                else if (obj instanceof Apartamento){
                    listadefinanciamentos.add((Apartamento) obj);
                }
                else if (obj instanceof Terreno){
                    listadefinanciamentos.add((Terreno) obj);
                }
            }
        } catch (EOFException ex) {
            ex.printStackTrace();
        } catch (ClassNotFoundException ex){
            ex.printStackTrace();
        } catch (FileNotFoundException ex){
            ex.printStackTrace();
        } catch (IOException ex){
            ex.printStackTrace();
        } finally {
            try {
                if (inputStream != null) {
                    inputStream.close();
                    System.out.println("Arquivo .dat lido com sucesso -- ArrayList populado!");
                }
            } catch (IOException ex){
                ex.printStackTrace();
            }
        }
    }
}
