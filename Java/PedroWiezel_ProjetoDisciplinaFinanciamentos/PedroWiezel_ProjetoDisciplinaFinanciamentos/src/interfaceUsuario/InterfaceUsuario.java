package interfaceUsuario;

import java.util.Scanner;
import java.util.Locale;

public class InterfaceUsuario {

    public static double coletar_valor_imovel() {
        Scanner coletor = new Scanner(System.in);
        coletor.useLocale(Locale.forLanguageTag("pt-BR"));
        double valorImovel = 0.0;
        boolean entradaValida = false;
        do {
            try {
                System.out.print("Digite o valor do imóvel: R$ ");
                valorImovel = Double.parseDouble(coletor.nextLine());
                if (valorImovel <= 0) {
                    throw new IllegalArgumentException("O valor do imóvel deve ser maior que zero.");
                }
                entradaValida = true;
            } catch (NumberFormatException e) {
                System.out.println("Por favor, digite um valor numérico válido.");
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        } while (!entradaValida);

        return valorImovel;
    }

    public static int coletar_prazo_financiamento() {
        Scanner coletor = new Scanner(System.in);
        coletor.useLocale(Locale.forLanguageTag("pt-BR"));
        int prazoFinanciamento = 0;
        boolean entradaValida = false;

        do {
            try {
                System.out.print("Digite o prazo do financiamento em anos: ");
                prazoFinanciamento = Integer.parseInt(coletor.nextLine());
                if (prazoFinanciamento <= 0) {
                    throw new IllegalArgumentException("O prazo do financiamento deve ser maior que zero.");
                }
                entradaValida = true;
            } catch (NumberFormatException e) {
                System.out.println("Por favor, digite um valor numérico válido.");
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        } while (!entradaValida);

        return prazoFinanciamento;
    }

    public static double coletar_taxa_juros_anual() {
        Scanner coletor = new Scanner(System.in);
        coletor.useLocale(Locale.forLanguageTag("pt-BR"));
        double taxaJuros = 0.0;
        boolean entradaValida = false;

        do {
            try {
                System.out.print("Digite a taxa de juros anual: ");
                taxaJuros = Double.parseDouble(coletor.nextLine());
                if (taxaJuros <= 0) {
                    throw new IllegalArgumentException("A taxa de juros deve ser maior que zero.");
                }
                entradaValida = true;
            } catch (NumberFormatException e) {
                System.out.println("Por favor, digite um valor numérico válido.");
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        } while (!entradaValida);

        return taxaJuros;
    }

    public static double coletarTamanhoTerreno() {
        Scanner coletor = new Scanner(System.in);
        coletor.useLocale(Locale.forLanguageTag("pt-BR"));
        double tamanhoTerreno = 0.0;
        boolean entradaValida = false;

        do {
            try {
                System.out.print("Digite o tamanho do terreno: ");
                tamanhoTerreno = Double.parseDouble(coletor.nextLine());
                if (tamanhoTerreno <= 0) {
                    throw new IllegalArgumentException("O tamanho do terreno tem que ser positivo.");
                }
                entradaValida = true;
            } catch (NumberFormatException e) {
                System.out.println("Por favor, digite um valor numérico válido.");
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        } while (!entradaValida);

        return tamanhoTerreno;
    }

    public static double coletarTamanhoConstruido() {
        Scanner coletor = new Scanner(System.in);
        coletor.useLocale(Locale.forLanguageTag("pt-BR"));
        double tamanhoConstruido = 0.0;
        boolean entradaValida = false;

        do {
            try {
                System.out.print("Digite a área construída: ");
                tamanhoConstruido = Double.parseDouble(coletor.nextLine());
                if (tamanhoConstruido <= 0) {
                    throw new IllegalArgumentException("O tamanho da área construída tem que ser positivo.");
                }
                entradaValida = true;
            } catch (NumberFormatException e) {
                System.out.println("Por favor, digite um valor numérico válido.");
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        } while (!entradaValida);

        return tamanhoConstruido;
    }

    public static int coletarNumeroVagasGaragem() {
        Scanner coletor = new Scanner(System.in);
        coletor.useLocale(Locale.forLanguageTag("pt-BR"));
        int vagasGaragem = 0;
        boolean entradaValida = false;

        do {
            try {
                System.out.print("Digite o número de vagas na garagem: ");
                vagasGaragem = Integer.parseInt(coletor.nextLine());
                if (vagasGaragem <= 0) {
                    throw new IllegalArgumentException("O tamanho da área construída tem que ser 0 ou mais.");
                }
                entradaValida = true;
            } catch (NumberFormatException e) {
                System.out.println("Por favor, digite um valor numérico válido.");
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        } while (!entradaValida);

        return vagasGaragem;
    }

    public static int coletarAndarApartamento() {
        Scanner coletor = new Scanner(System.in);
        coletor.useLocale(Locale.forLanguageTag("pt-BR"));
        int andar = 0;
        boolean entradaValida = false;

        do {
            try {
                System.out.print("Digite o andar do apartamento: ");
                andar = Integer.parseInt(coletor.nextLine());
                if (andar <= 0) {
                    throw new IllegalArgumentException("O andar tem que ser positivo.");
                }
                entradaValida = true;
            } catch (NumberFormatException e) {
                System.out.println("Por favor, digite um valor numérico válido.");
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        } while (!entradaValida);

        return andar;
    }

    public static String coletarZona() {
        Scanner coletor = new Scanner(System.in);
        coletor.useLocale(Locale.forLanguageTag("pt-BR"));
        int zona = 0;
        boolean entradaValida = false;

        do {
            try {
                System.out.print("Qual a zona do terreno? 1 - Residencial ou 2 - Comercial?: ");
                zona = Integer.parseInt(coletor.nextLine());
                if (zona != 1 && zona != 2) {
                    throw new IllegalArgumentException("Escolha uma das duas opções.");
                }
                entradaValida = true;
            } catch (NumberFormatException e) {
                System.out.println("Por favor, digite um valor numérico válido.");
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        } while (!entradaValida);

        if (zona == 1) { return "RESIDENCIAL"; }
        else if (zona == 2) { return "COMERCIAL"; }
        else return null;
    }
}